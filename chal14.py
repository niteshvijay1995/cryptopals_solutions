import chal11
import chal9
import chal7
import base64
from Crypto.Random import random
KEY = ''

unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

#Assumption - Size of random-prefix is same
random_prefix = ''

def encryption_oracle(plaintext):
	plaintext = random_prefix+plaintext+base64.b64decode(unknown_string)
	plaintext = chal9.pad(plaintext,16)
	return chal7.encrypt_ECB(plaintext,KEY)

def check_ECB_block_size():
	length = 1
	plaintext = 'A'
	last_cipher = len(encryption_oracle(plaintext))
	while True:
		plaintext += 'A'
		cipher = len(encryption_oracle(plaintext))
		if cipher > last_cipher:
			return cipher - last_cipher
		last_cipher = cipher
		length += 1
	return length

def get_prefix_length(block_length):
	cipher1 = encryption_oracle('A')
	cipher2 = encryption_oracle('B')
	i = 0
	matched_size = 0
	while True:
		if cipher1[i*block_length:(i+1)*block_length] != cipher2[i*block_length:(i+1)*block_length]:
			break
		i += 1
	matched_size = i*block_length
	for k in range(1,block_length+1):
		cipher1 = encryption_oracle('A'*(k+1))
		cipher2 = encryption_oracle('A'*k+'B')
		if cipher1[matched_size:matched_size+block_length] == cipher2[matched_size:matched_size+block_length]:
			break
	matched_size += (block_length-k)
	return matched_size

def break_ECB():
	matched_string = ''
	block_length = check_ECB_block_size()
	prefix_len = get_prefix_length(block_length)
	prefix_block_len = (prefix_len/block_length)*block_length
	size_of_msg = len(encryption_oracle('')) - prefix_len
	msg_blocks = (size_of_msg/block_length)*block_length
	#print msg_blocks,' ',size_of_msg
	for k in range(size_of_msg):
		#print len(matched_string)
		plaintext = 'A'*(msg_blocks-len(matched_string)-1+prefix_block_len-prefix_len)
		ciphertext = encryption_oracle(plaintext)[prefix_block_len:prefix_block_len+msg_blocks]
		for i in range(256):
			if ciphertext == encryption_oracle(plaintext+matched_string+chr(i))[prefix_block_len:prefix_block_len+msg_blocks]:
				matched_string += chr(i)
				break
	return matched_string

if __name__=="__main__":
	KEY = chal11.get_random_bytes(16)
	random_prefix = chal11.get_random_bytes(random.randint(1,100))
	#print check_ECB_block_size()
	print break_ECB()
