import chal10
import chal11
from SHA1 import SHA1
import socket
import json
from random import randint
import binascii
s = socket.socket()
host = socket.gethostname()
port = int(raw_input('Port - '))
s.bind(('127.0.0.1',port))
s.listen(5)
c,addr = s.accept()
print "Connected to B"
p = 'ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff'
p = int(p,16)
g = 2
a = randint(1,p)
A = pow(g,a,p)
packet = {}
packet['p'] = p
packet['g'] = g
packet['A'] = A
c.send(json.dumps(packet))
print "p,g,A sent to B"
response = json.loads(c.recv(1024))
B = response['B']
print 'B received'
msg = "Hello B"
s = pow(B,a,p)
hash = SHA1()
hash.update(str(s))
key = hash.hexdigest()[0:16]
#print key
iv = chal11.get_random_bytes(16)
#print 'iv - ',iv
cipher = chal10.encrypt_CBC(msg,key,iv)
cipher = iv + cipher
#print cipher
c.send(cipher)
response = c.recv(1024)
cipher = response[16:]
iv = response[:16]
msg = chal10.decrypt_CBC(cipher,key,iv)
print 'Message from B - ',msg
c.close()
