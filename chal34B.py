import socket
import json
import chal10
import chal11
from random import randint
from SHA1 import SHA1
import binascii
s = socket.socket()
host = '127.0.0.1'
port = int(raw_input('Port - '))
s.connect((host, port))
packet = s.recv(1024)
#print packet
packet = json.loads(packet)
A = packet['A']
p = packet['p']
g = packet['g']
b = randint(1,p)
B = pow(g,b,p)
response = {}
response['B'] = B
s.send(json.dumps(response))
sb = pow(A,b,p)
hash = SHA1()
hash.update(str(sb))
key = hash.hexdigest()[0:16]
'''packet = json.loads(s.recv(1024))
cipher = binascii.unhexlify(packet['cipher'])
iv = packet['iv']
'''
cipher = s.recv(2048)
iv = cipher[0:16]
cipher = cipher[16:]
#print 'iv - ',iv
#print 'cipher - ',cipher
msg = chal10.decrypt_CBC(cipher,key,iv)
print 'Message from A - ',msg
msg = "Hello A"
iv = chal11.get_random_bytes(16)
cipher = chal10.encrypt_CBC(msg,key,iv)
cipher = iv + cipher
s.send(cipher)
s.close
