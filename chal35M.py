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
g = packet['g']
p = packet['p']

#forgery
#packet['g'] = 1
#packet['g'] = p
packet['g'] = p
c.send(json.dumps(packet))
print "p,g sent to B"

response = c.recv(1024)		#ack from B
s1.send(response)

packet = s1.recv(1024)		#A value from A
packet = json.loads(packet)
#packet['A'] = 1		#g = 1
#packet['A'] = p 	#g = p
A = packet['A']

c.send(json.dumps(packet))

response = c.recv(1024)		#B value from B
B = json.loads(response)['B']
s1.send(response)

#Due to forgery s will become 1 
#sM = 1			#g = 1
#sM = 0			#g = p
#g = p-1
if B==p-1:
	sM = p-1
else:
	sM = 1
print 'sM = ',sM
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
