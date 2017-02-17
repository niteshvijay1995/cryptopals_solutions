from Crypto.Random import random
import chal7
import chal9
import chal10


def get_random_bytes(k):
	res = ''
	for i in range(k):
		res += chr(random.getrandbits(8))
	return res

def encryption_oracle(plaintext):
	aes_key = get_random_bytes(16)
	plaintext = get_random_bytes(random.randint(5,10))+plaintext+get_random_bytes(random.randint(5,10))
	ecb_flag = (0==random.randint(0,1))
	#print ecb_flag
	if ecb_flag:
		#ecb encryption
		plaintext = chal9.pad(plaintext,16)
		return chal7.encrypt_ECB(plaintext,aes_key)
	else:
		iv = get_random_bytes(16)
		return chal10.encrypt_CBC(plaintext,aes_key,iv)
		#cbc encryption

def check_ECB(ciphertext):
	BLOCK_SIZE  = 16
	length = len(ciphertext)
	blocks = length/BLOCK_SIZE
	for i in range(blocks):
		for j in range(i+1,blocks):
			if ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE] == ciphertext[j*BLOCK_SIZE:(j+1)*BLOCK_SIZE]:
				return True
	return False

def check_encryption_function(ciphertext):
	if check_ECB(ciphertext):
		return "ECB"
	return "CBC"

if __name__=="__main__":
	plaintext = "D"*50
	ciphertext = encryption_oracle(plaintext)
	print check_encryption_function(ciphertext)
