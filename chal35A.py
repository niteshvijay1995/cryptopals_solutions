import chal10
import chal11
from SHA1 import SHA1
import socket
import json
from random import randint
import binascii

#Client

class Server:
	key = ''
	s = socket.socket()
	c = ''
	def __init__(self):
		port = int(raw_input('Port - '))
		self.s.bind(('127.0.0.1',port))
		self.s.listen(5)
		print 'Listening ...'
		self.c,addr = self.s.accept()
		print 'Connected to server at',addr
	def key_negotiation(self):
		p = 'ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff'
		p = int(p,16)
		g = 2
		packet = {}
		packet['p'] = p
		packet['g'] = g
		#packet['A'] = A
		self.c.send(json.dumps(packet))
		response = self.c.recv(1024)
		try:
			response = json.loads(response)
		except Exception as e:
			print 'Key negotiation failed'
			return
		p_final = response['p']
		g_final = response['g']
		a = randint(1,p_final)
		A = pow(g_final,a,p_final)
		packet = {}
		packet['A'] = A
		self.c.send(json.dumps(packet))
		try:
			response = json.loads(self.c.recv(1024))
		except Exception as e:
			print 'Key negotiation failed'
			return
		B = response['B']
		s = pow(B,a,p_final)
		hash = SHA1()
		hash.update(str(s))
		self.key = hash.hexdigest()[0:16]
		print'Key negotiation completed successfully'
	def send_msg(self,msg):
		iv = chal11.get_random_bytes(16)
		#print 'iv - ',iv
		cipher = chal10.encrypt_CBC(msg,self.key,iv)
		cipher = iv + cipher
		#print cipher
		self.c.send(cipher)
	def recv_msg(self):
		response = self.c.recv(1024)
		cipher = response[16:]
		iv = response[:16]
		return chal10.decrypt_CBC(cipher,self.key,iv)
	def close(self):
		self.c.close()

if __name__ == "__main__":
	foo = Server()
	foo.key_negotiation()
	msg = raw_input('Send message to bar - \nFoo : ')
	foo.send_msg(msg)
	print 'Waiting for message from bar ...'
	msg = foo.recv_msg()
	print 'Bar : ',msg
