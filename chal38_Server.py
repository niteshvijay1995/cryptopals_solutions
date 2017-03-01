import random
import hashlib
import socket
import json
import hmac
import base64
N = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 2
k = 3
class Server:
	s = socket.socket()
	def __init__(self):
		port = int(raw_input('Port - '))
		self.s.bind(('127.0.0.1',port))
		self.s.listen(5)
		print 'Listening ...'
		self.c,addr = self.s.accept()
		print 'Connected to client at',addr
	def run(self):
		password = 'YW1iaWd1aXR5'
		password = base64.b64decode(password)
		salt = random.randint(0,2**32-1)
		sha256 = hashlib.sha256(str(salt)+password)
		xH = sha256.hexdigest()
		x = int(xH,16)
		v = pow(g,x,N)
		response = self.c.recv(1024)
		response = json.loads(response)
		#print response
		A = response['A']
		I = response['I']
		packet = {}
		packet['salt'] = salt
		b = random.randint(1,N)
		B = pow(g,b,N)
		packet['B'] = B
		u = random.randint(0,2**128-1)
		packet['u'] = u
		#print 'Sending - ',packet
		self.c.send(json.dumps(packet))
		#print u
		S = pow((A*pow(v,u,N)),b,N)
		#print S
		K = hashlib.sha256(str(S)).hexdigest()
		hmac_val_from_client = self.c.recv(1024)
		print 'Rec...'
		if hmac.new(str(K),str(salt)).hexdigest() == hmac_val_from_client:
			self.c.send("OK")
		else:
			self.c.send("Invalid")

	def close(self):
		self.c.close()
if __name__ == "__main__":
	s = Server()
	s.run()
	s.close()