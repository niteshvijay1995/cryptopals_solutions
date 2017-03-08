import math
import random
import math
import chal39
priv_key = None

def get_random_bytes_without_zero(k):
	res = ''
	for i in range(k):
		c = '\x00'
		while c=='\x00':
			c = chr(random.getrandbits(8))
		res += c
	return res

def PKCS_pad(data,pub_key):
	_,n = pub_key
	k = int(math.ceil(n.bit_length()/8.0))
	return '\x00\x02'+get_random_bytes_without_zero(k-3-len(data))+'\x00'+data

def PKCS_unpad(data,pub_key):
	_,n = pub_key
	k = int(math.ceil(n.bit_length()/8.0))
	data = b'\x00'*(k-len(data))+data
	if data[0:2] == '\x00\x02':
		data = data[2:]
		return data[data.index('\x00'):]
	else:
		raise Exception('Padding Error')

def oracle(ciphertext,pub_key):
	_,n = pub_key
	plain_text = chal39.rsa_decrypt_str(ciphertext,priv_key)
	k = int(math.ceil(n.bit_length()/8.0))
	plain_text = b'\x00'*(k-len(plain_text))+plain_text
	return plain_text[0]=='\x00' and plain_text[1]=='\x02'

def getFirsts(c0,pub_key,B):
	e,n = pub_key
	s = (n+3*B-1)/(3*B)
	while True:
		c = (c0*pow(s,e,n))%n
		if oracle(c,pub_key):
			return s
		s += 1

def getNexts(s_prev,c0,M,B,pub_key):
	e,n = pub_key
	if len(M)>1:
		s = s_prev
		while True:
			c = (c0*pow(s,e,n))%n
			if oracle(c,pub_key):
				return s
			s += 1
	else:
		a,b = M[0]
		r = (2*(b*s_prev - 2*B)+n-1)/n
		while True:
			for si in range((2*B+r*n+b-1)/b,(3*B+r*n+a-1)/a):
				if oracle((c0*pow(si,e,n))%n,pub_key):
					return si
			r += 1

def getM(s,M,pub_key,B):
	e,n = pub_key
	M_ret = []
	for a,b in M:
		rmin = (a*s-3*B+1+n-1)/n
		rmax = (b*s-2*B+n-1)/n
		for r in range(rmin,rmax):
			ai = max(a,(2*B+r*n+s-1)/s)
			bi = min(b,(3*B-1+r*n)/s)
			if ai>bi:
				continue
			M_ret.append((ai,bi))
	return M_ret


def attack(c,pub_key):
	print 'Cracking ...'
	e,n = pub_key
	k = int(math.ceil(n.bit_length()/8.0))
	B = 2**(8*(k-2))
	M = [(2*B,3*B-1)]
	s = getFirsts(c,pub_key,B)
	M = getM(s,M,pub_key,B)
	while True:
		if len(M)==1:
			a,b = M[0]
			print chal39.num_to_str(a)
			if a == b:
				return a
		s = getNexts(s,c,M,B,pub_key)
		M = getM(s,M,pub_key,B)

pub_key,priv_key = chal39.genKey(768)
m = "kick it, CC"
c = chal39.rsa_encrypt_str(PKCS_pad(m,pub_key),pub_key)
print "Oracle Test : ",oracle(c,pub_key)
plain_text = chal39.num_to_str(attack(c,pub_key))
print "Cracked Plaintext - ",PKCS_unpad(plain_text,pub_key)



