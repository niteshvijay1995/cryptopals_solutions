#RSA
import binascii
from Crypto.Util import number

def egcd(a,b):
	if a == 0:
		return (b,0,1)
	else:
		g,y,x = egcd(b%a, a)
		return (g,x-(b // a)*y, y)

def invmod(a,N):		#	1/a mod N
	g,x,y = egcd(a,N)
	if g!=1:
		raise Exception("Modular Inverse doesn't exist")
	else:
		return x%N

prime_table = [2,3,5,7,11,13,17,23]

def genKey(length):
	e = 3
	while True:
		try:
			p = number.getPrime(length)
			q = number.getPrime(length)
			n = p*q
			et = (p-1)*(q-1)
			d = invmod(e,et)
			break
		except:
			continue
	return [e,n],[d,n]

def rsa_encrypt(data,key):
	e = key[0]
	n = key[1]
	if data<0 or data>n:
		raise Exception(str(data)+": Out of bound- Hint: Increase your key size")
	return pow(data,e,n)

def rsa_decrypt(cipher,key):
	d = key[0]
	n = key[1]
	if cipher<0 or cipher>n:
		raise Exception("Out of bound message - Hint: Increase your key size")
	return pow(cipher,d,n)

def str_to_num(a):
	return int(binascii.hexlify(a),16)

def num_to_str(n):
	n = hex(n)[2:]
	if n[-1] == 'L':
		n = n[:-1]
	if len(n)%2 != 0:
		n = '0'+n
	return binascii.unhexlify(n)

def rsa_encrypt_str(data,key):
	return rsa_encrypt(str_to_num(data),key)

def rsa_decrypt_str(cipher,key):
	return num_to_str(rsa_decrypt(cipher,key))

if __name__=="__main__":
	#tests
	if egcd(38,73) == (1,25,-13):
		print "Test#1 passed"
	else:
		print "Test#1 failed"

	if egcd(1,0) == (1,1,0):
		print "Test#2 passed"
	else:
		print "Test#2 failed"

	if invmod(17,3120) == 2753:
		print "Test#3 passed"
	else:
		print "Test#3 failed"

	if invmod(13,5) == 2:
		print "Test#4 passed"
	else:
		print "Test#4 failed"

	print "String_num_conversion test : ","Hello World"== num_to_str(str_to_num("Hello World"))

	print "RSA Test : "

	pub_key,priv_key = genKey(200)

	print 'Test#1 : ',4271262121 == rsa_decrypt(rsa_encrypt(4271262121,pub_key),priv_key)
	print 'Test#2 : ',"FlockOS" == rsa_decrypt_str(rsa_encrypt_str("FlockOS",pub_key),priv_key)



