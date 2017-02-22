import socket
import json
import chal10
from SHA1 import SHA1

s1 = socket.socket()
s2 = socket.socket()
host = '127.0.0.1'
port1 = int(raw_input('Port1 (Connection to A) - '))
port2 = int(raw_input('Port2 (Connection to B) - '))

s2.bind(('127.0.0.1',port2))
s2.listen(5)
c,addr = s2.accept()

s1 = socket.socket()
s1.connect((host, port1))

packet = s1.recv(1024)
packet = json.loads(packet)
A = packet['A']
p = packet['p']

#forgery
packet['A'] = p
c.send(json.dumps(packet))
print "p,g,A sent to B"

response = json.loads(c.recv(1024))
response['B'] = p
s1.send(json.dumps(response))

#Due to forgery s will become 0
sM = 0
hash = SHA1()
hash.update(str(sM))
key = hash.hexdigest()[0:16]


cipher = s1.recv(2048)
c.send(cipher)
iv = cipher[0:16]
cipher = cipher[16:]
msg = chal10.decrypt_CBC(cipher,key,iv)
print 'Message from A (Cracked)- ',msg

response = c.recv(1024)
s1.send(response)
cipher = response[16:]
iv = response[:16]
msg = chal10.decrypt_CBC(cipher,key,iv)
print 'Message from B (Cracked)- ',msg

c.close()
s1.close
