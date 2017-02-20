import chal9
import chal10
import chal11
import chal18
KEY = ''
nonce = 0

import chal9
import chal10
import chal11
from fractions import gcd
from random import randint
KEY = ''
nonce = 0
def ctr_oracle(plaintext):
	plaintext = plaintext.replace(';','')
	plaintext = plaintext.replace('=','')
	plaintext = "comment1=cooking%20MCs;userdata="+plaintext+";comment2=%20like%20a%20pound%20of%20bacon"
	#plaintext = chal9.pad(plaintext,16)
	return chal18.encrypt_decrypt_CTR(plaintext,KEY,nonce)

def decrypt_oracle(ciphertext):
	plaintext = chal18.encrypt_decrypt_CTR(ciphertext,KEY,nonce)
	s_elements = plaintext.split(';')
	print s_elements
	if 'admin=true' in s_elements:
		return True
	else:
		return False

def break_ctr():

	#Check fixed length of prefix
	cipher1 = ctr_oracle("")
	cipher2 = ctr_oracle("X")

	prefix_len = 0
	for c in cipher2:
		if cipher1[prefix_len] == c:
			prefix_len += 1
		else:
			break

	cipher = list(ctr_oracle(">admin<true>"))
	cipher[prefix_len] = chr(ord(cipher[prefix_len])^ord('>')^ord(';'))
	cipher[prefix_len+6] = chr(ord(cipher[prefix_len+6])^ord('<')^ord('='))
	cipher[prefix_len+11] = chr(ord(cipher[prefix_len+11])^ord('>')^ord(';'))

	ciphertext = ''.join(c for c in cipher)
	if decrypt_oracle(ciphertext):
		print "Oracle cracked"
	else:
		print "Failed"

if __name__=="__main__":
	KEY = chal11.get_random_bytes(16)
	nonce = 0
	#Test functions
	cipher = ctr_oracle(";admin=true;")
	if decrypt_oracle(cipher):
		print "Test Failed ! (String found)"
	else:
		print "Test passed"
	
	break_ctr()
