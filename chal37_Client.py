import socket
import hashlib
import hmac
import random
import json
N = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 2
k = 3
class Client:
	s = socket.socket()
	key = ''
	def __init__(self):
		host = '127.0.0.1'
		port = int(raw_input('Port - '))
		self.s.connect((host, port))
		print 'Connected to Server :)'
	
	def run(self):
		I = raw_input('Email - ')
		#P = raw_input('Password - ')
		#a = random.randint(1,N)
		#A = pow(g,a,N)
		A = N*int(raw_input('A (N will be multiplied to the value) - '))
		packet = {}
		packet['I'] = I
		packet['A'] = A
		self.s.send(json.dumps(packet))
		response = self.s.recv(1024)
		#print response
		response = json.loads(response)
		B = response['B']
		salt = response['salt']
		#uH = hashlib.sha256(str(A)+str(B)).hexdigest()
		#u  = int(uH,16)
		#print 'u - ',u
		#xH = hashlib.sha256(str(salt)+P).hexdigest()
		#x = int(xH,16)
		#print 'x - ',x
		#S = pow((B-k*pow(g,x,N)),(a+u*x),N)
		S = 0
		K = hashlib.sha256(str(S)).hexdigest()
		hmac_val = hmac.new(str(K),str(salt)).hexdigest()
		#print 'Sending - ',hmac_val
		self.s.send(hmac_val)
		print self.s.recv(1024)
	def close(self):
		self.s.close

if __name__ == "__main__":
	c = Client()
	c.run()
	c.close()