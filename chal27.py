import chal9
import chal10
import chal11
from fractions import gcd
from random import randint
KEY = ''
iv = ''
def cbc_oracle(plaintext):
	plaintext = plaintext.replace(';','')
	plaintext = plaintext.replace('=','')
	plaintext = "comment1=cooking%20MCs;userdata="+plaintext+";comment2=%20like%20a%20pound%20of%20bacon"
	plaintext = chal9.pad(plaintext,16)
	return chal10.encrypt_CBC(plaintext,KEY,iv)

def decrypt_oracle(ciphertext):
	plaintext = chal10.decrypt_CBC(ciphertext,KEY,iv)		#The function will implicitly check for correct padding

	if any([c>127 for c in plaintext]):
		raise Exception(plaintext)
	s_elements = plaintext.split(';')
	print s_elements
	if 'admin=true' in s_elements:
		return True
	else:
		return False
'''
def check_block_size():
	length = 0
	for i in range(256):
		if length == 0:
			length = len(cbc_oracle('A'*randint(0,256)))
		else:
			length = gcd(length,len(cbc_oracle('A'*randint(0,256))))
	return length

def break_cbc():

	block_size = check_block_size()

	print "BLOCK SIZE = ",block_size
	#Check fixed length of prefix
	cipher1 = cbc_oracle("")
	cipher2 = cbc_oracle("X")

	prefix_len = 0
	for c in cipher2:
		if cipher1[prefix_len] == c:
			prefix_len += 1
		else:
			break

	cipher = list(cbc_oracle(">admin<true>"))
	cipher[prefix_len-block_size] = chr(ord(cipher[prefix_len-block_size])^ord('>')^ord(';'))
	cipher[prefix_len-block_size+6] = chr(ord(cipher[prefix_len-block_size+6])^ord('<')^ord('='))
	cipher[prefix_len-block_size+11] = chr(ord(cipher[prefix_len-block_size+11])^ord('>')^ord(';'))

	ciphertext = ''.join(c for c in cipher)
	if decrypt_oracle(ciphertext):
		print "Oracle cracked"
	else:
		print "Failed"


'''

def break_cbc():
	cipher = cbc_oracle("random")
	cipher = cipher[:16]+'\x00'*16+cipher[:16]+cipher[48:]
	try:
		decrypt_oracle(cipher)
		print "Failed"
	except Exception as e:
		e = e.args[0]
		cracked_key = chal10.xor_data(e[0:16],e[32:48])
		#print KEY,cracked_key
		if cracked_key == KEY:
			print "Oracle Cracked :)     Key - ",cracked_key




if __name__=="__main__":

	#iv = chal11.get_random_bytes(16)
	KEY = chal11.get_random_bytes(16)
	iv = KEY

	#Test functions
	#cipher = cbc_oracle(";admin=true;")
	#if decrypt_oracle(cipher):
	#	print "Test Failed ! (String found)"
	#else:
	#	print "Test passed"
	
	break_cbc()