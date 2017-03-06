
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
	k = random.randint(1,q)
	r = pow(g,k,p)%q
	s = (chal39.invmod(k,q)*(int(H(msg),16) + x*r))%q
	return r,s

def verify(msg,sign,pub_key):
	r,s = sign
	y = pub_key
	w = chal39.invmod(s,q)
	u1 = (int(H(msg),16)*w)%q
	u2 = (r*w)%q
	v = ((pow(g,u1,p)*pow(y,u2,p))%p)%q
	return v==r


if __name__ == "__main__":
	x = random.randint(1,q)
	
	#g = 0, therefore r = 0
	print "------g=0-------"
	g = 0
	msg1 = "Hello, world"
	msg2 = "Goodbye, world"
	sign1 = dsa_signing(msg1,x)
	sign2 = dsa_signing(msg2,x)
	print "Sign1 : ",sign1
	print "Sign2 : ",sign2
	print "DSA Test#1 - ",verify(msg1,sign1,get_pub_key(x))
	print "DSA Test#2 - ",verify(msg2,sign1,get_pub_key(x))
	print "DSA Test#3 - ",verify(msg1,sign2,get_pub_key(x))
	print "DSA Test#4 - ",verify(msg2,sign2,get_pub_key(x))

	#g=p+1
	print "------g=p+1-------"
	g = p+1
	y = get_pub_key(x)
	z = random.randint(1,10)
	print "z = ",z
	r = pow(y,z,p)%q
	s = r%q * chal39.invmod(z,q)
	sign = r,s
	print "Sign : ",sign
	print "DSA Test#1 - ",verify(msg1,sign,get_pub_key(x))
	print "DSA Test#2 - ",verify(msg2,sign,get_pub_key(x))


