import base64
import chal39
import math

plaintext = "VGhhdCdzIHdoeSBJIGZvdW5kIHlvdSBkb24ndCBwbGF5IGFyb3VuZCB3aXRoIHRoZSBGdW5reSBDb2xkIE1lZGluYQ=="
priv_key = None

def oracle(ciphertext):				#return true for even
	return chal39.rsa_decrypt(ciphertext,priv_key)%2==0


if __name__=="__main__":
	pub_key,priv_key = chal39.genKey(1024)
	plaintext = base64.b64decode(plaintext)
	ciphertext = chal39.rsa_encrypt_str(plaintext,pub_key)
	e,n = pub_key
	upper_bound = 1
	lower_bound = 0
	denom = 1
	factor = pow(2,e,n)
	print "Computing..."
	for i in range(n.bit_length()):
		ciphertext = (ciphertext*factor)%n
		denom *= 2
		if oracle(ciphertext):
			upper_bound = (upper_bound+lower_bound)
			lower_bound *= 2
		else:
			lower_bound = (upper_bound+lower_bound)
			upper_bound *= 2
		print chal39.num_to_str(n*upper_bound/denom)	

	print chal39.num_to_str(n*upper_bound/denom)