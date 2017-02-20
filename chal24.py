import chal21
import chal11
import random
import time
def encrypt(key,plaintext):
	r = chal21.random_number()
	r.seed_mt(key)			#seed = key
	ciphertext = ''
	for c in plaintext:
		ciphertext += chr(ord(c) ^ r.extract_number()%256)
	return ciphertext

def decrypt(key,ciphertext):
	return encrypt(key,ciphertext)

def break_cipher(ciphertext):
	suffix_plaintext = 'A'*14
	for seed in range(2**16-1):
		#print '.',
		if decrypt(seed,ciphertext)[-14:] == suffix_plaintext:
			print 'Cipher Cracked :)'
			return seed

def generate_pass_link():
	plaintext = 'A'*14
	return encrypt(int(time.time()),plaintext)

def check_pass_link(ciphertext):
	return decrypt(int(time.time()),ciphertext) == 'A'*14 

if __name__ == "__main__":
	plaintext = chal11.get_random_bytes(random.randint(2,40)) + 'A'*14
	key = random.randint(0,2**16-1)
	ciphertext  = encrypt(key,plaintext)
	print "Key Matched - ",key==break_cipher(ciphertext)

	print 'Password link time seed test -',check_pass_link(generate_pass_link())
