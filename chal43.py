
import random
import hashlib
import chal39
p = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
x = 1
def H(data):
	return hashlib.sha1(data).hexdigest()

def get_pub_key(x):
	return pow(g,x,p)

def dsa_signing(msg,x):
	r = 0
	s = 0
	while s==0:
		while r==0:
			k = random.randint(1,q)
			r = pow(g,k,p)%q
		s = (chal39.invmod(k,q)*(int(H(msg),16) + x*r))%q
	return r,s

def verify_key(priv,pub):
	return pub == pow(g,priv,p)

def verify(msg,sign,pub_key):
	r,s = sign
	y = pub_key
	w = chal39.invmod(s,q)
	u1 = (int(H(msg),16)*w)%q
	u2 = (r*w)%q
	v = ((pow(g,u1,p)*pow(y,u2,p))%p)%q
	return v==r

def attack(msg):
	print "Attacking ..."
	r = 548099063082341131477253921760299949438196259240
	s = 857042759984254168557880549501802188789837994940
	y = 0x84ad4719d044495496a3201c8ff484feb45b962e7302e56a392aee4abab3e4bdebf2955b4736012f21a08084056b19bcd7fee56048e004e44984e2f411788efdc837a0d2e5abb7b555039fd243ac01f0fb2ed1dec568280ce678e931868d23eb095fde9d3779191b8c0299d6e07bbb283e6633451e535c45513b2d33c99ea17
	print "Test1 - ",'d2d0714f014a9784047eaeccf956520045c45265'==H(msg)
	h =  0xd2d0714f014a9784047eaeccf956520045c45265
	for k in range(0,2**16):
		x = (((s*k) - h)%q * chal39.invmod(r,q))%q
		if verify_key(x,y):
			print "Cracked :)"
			return x


if __name__ == "__main__":
	x = random.randint(1,q)
	msg = '''For those that envy a MC it can be hazardous to your health
So be friendly, a matter of life and death, just like a etch-a-sketch
'''
	print "DSA Test - ",verify(msg,dsa_signing(msg,x),get_pub_key(x))
	priv_key = attack(msg)
	print "Key Hash test - ", H(hex(priv_key)[2:-1]) == "0954edd5e0afe5542a4adf012611a91912a3ec16"
	print "Signature test - ", verify(msg,dsa_signing(msg,priv_key),get_pub_key(priv_key))