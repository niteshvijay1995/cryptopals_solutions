import socket
import json
import chal10
import hashlib
import hmac

N = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 2
k = 3

s1 = socket.socket()
s2 = socket.socket()
host = '127.0.0.1'
port1 = int(raw_input('Port1 (Connection to Server) - '))
port2 = int(raw_input('Port2 (Connection to Client) - '))

s2.bind(('127.0.0.1',port2))
s2.listen(5)
c,addr = s2.accept()

s1 = socket.socket()
s1.connect((host, port1))

response = c.recv(1024)
response = json.loads(response)
I = response['I']
A = response['A']

s1.send(json.dumps(response))

packet = s1.recv(1024)
packet = json.loads(packet)

salt = packet['salt']
B = packet['B']

forged_b = 3
forged_B = pow(g,forged_b,N)
packet['B'] = forged_B

u = packet['u']
forged_u = 1

packet['u'] = forged_u 
c.send(json.dumps(packet))


response = c.recv(1024)
hmac_client = response

words_dict = open("/usr/share/dict/words").readlines()

first_letter = 'a'
print first_letter,'....'
for word in words_dict:
	word = word.strip().lower()
	if first_letter != word[0]:
		first_letter = word[0]
		print first_letter,'....'
	x = int(hashlib.sha256(str(salt)+word).hexdigest(),16)
	v = pow(g,x,N)
	S = pow(A*pow(v,forged_u,N),forged_b,N)
	K = hashlib.sha256(str(S)).hexdigest()
	if hmac.new(str(K),str(salt)).hexdigest() == hmac_client:
		print "Password Cracked :) \nPassword - ",word
		break

c.close()
s1.close
