import chal11
import chal9
import chal7
import base64

KEY = ''

unknown_string = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

def encryption_oracle(plaintext):
	plaintext = plaintext+base64.b64decode(unknown_string)
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


def break_ECB():
	matched_string = ''
	block_length = check_ECB_block_size()
	size_of_msg = len(encryption_oracle(''))
	msg_blocks = (size_of_msg/block_length)*block_length
	#print msg_blocks,' ',size_of_msg
	for k in range(size_of_msg):
		#print len(matched_string)
		plaintext = 'A'*(msg_blocks-len(matched_string)-1)
		ciphertext = encryption_oracle(plaintext)[:msg_blocks]
		for i in range(256):
			if ciphertext == encryption_oracle(plaintext+matched_string+chr(i))[:msg_blocks]:
				matched_string += chr(i)
				break
	return matched_string

if __name__=="__main__":
	KEY = chal11.get_random_bytes(16)
	#print check_ECB_block_size()
	plaintext = break_ECB()
	print plaintext


