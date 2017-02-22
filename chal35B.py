import socket
import json
import chal10
import chal11
from random import randint
from SHA1 import SHA1
import binascii

class Client:
	s = socket.socket()
	key = ''
	def __init__(self):
		host = '127.0.0.1'
		port = int(raw_input('Port - '))
		self.s.connect((host, port))

	def key_negotiation(self):
		packet = self.s.recv(1024)
		#print packet
		try:
			packet = json.loads(packet)
		except Exception as e:
			print "Key negotiation failed"
			return False
		p = packet['p']
		g = packet['g']
		self.s.send(json.dumps(packet))
		packet = self.s.recv(1024)
		try:
			packet = json.loads(packet)
		except Exception as e:
			print "Key negotiation failed"
			return False
		A = packet['A']
		b = randint(1,p)
		B = pow(g,b,p)
		response = {}
		response['B'] = B
		self.s.send(json.dumps(response))
		s = pow(A,b,p)
		hash = SHA1()
		hash.update(str(s))
		self.key = hash.hexdigest()[0:16]

	def recv_msg(self):
		cipher = self.s.recv(2048)
		iv = cipher[0:16]
		cipher = cipher[16:]
		#print 'iv - ',iv
		#print 'cipher - ',cipher
		return chal10.decrypt_CBC(cipher,self.key,iv)
	def send_msg(self,msg):
		iv = chal11.get_random_bytes(16)
		cipher = chal10.encrypt_CBC(msg,self.key,iv)
		cipher = iv + cipher
		self.s.send(cipher)

	def close(self):
		self.s.close

if __name__ == "__main__":
	bar = Client()
	bar.key_negotiation()
	print 'Foo : ',bar.recv_msg()
	msg = raw_input('Bar : ')
	bar.send_msg(msg)
	bar.close()