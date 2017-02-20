import chal11
import chal9
import chal10
from Crypto.Random import random
import base64 

iv = ''
aes_key = ''

random_strings = ['MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=',
'MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=',
'MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==',
'MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==',
'MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl',
'MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==',
'MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==',
'MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=',
'MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=',
'MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93']

def CBC_padding_oracle_encrypt(key):
	plaintext = base64.b64decode(random_strings[random.randint(0,len(random_strings)-1)])
	print '.',
	iv = chal11.get_random_bytes(16)
	plaintext = chal9.pad(plaintext,16)
	ciphertext = chal10.encrypt_CBC(plaintext,key,iv)
	return ciphertext,iv

def check_CBC_padding_oracle(ciphertext,key,iv):
	try:
		palintext = chal10.decrypt_CBC(ciphertext,key,iv)
		return True
	except:
		return False

def change_last_bytes(block,last_bytes,guess_bytes):
	return block[:-len(guess_bytes)]+chal10.xor_data(guess_bytes,chal10.xor_data(block[-len(last_bytes):],last_bytes))


def break_block(curr_block,prev_block,ciphertext,key,iv):
	guess_block = ''
	'''for j in range(0,255):
		if check_CBC_padding_oracle(curr_block,key,change_last_bytes(iv,'\x01',chr(j))):
			guess_block = chr(j)+guess_block
			break
	for j in range(0,255):
		if check_CBC_padding_oracle(curr_block,key,change_last_bytes(iv,'\x02\x02',chr(j)+guess_block)):
			guess_block = chr(j)+guess_block
			print 'gb-',guess_block,' char-',j
			break
	for k in range(3,16):
		for j in range(0,255):
			
			if check_CBC_padding_oracle(curr_block,key,change_last_bytes(iv,chr(pad)*pad,chr(j)+guess_block)):
				guess_block = chr(j)+guess_block
				print 'gb-',len(guess_block),' char-',j
				break
		else:'''
		#print len(prev_block)
	possible_last_bytes = []
	for j in range(0,256):
		if check_CBC_padding_oracle(curr_block,key,change_last_bytes(prev_block,'\x01',chr(j))):
			#guess_block = chr(j)+guess_block
			possible_last_bytes.append(chr(j))
			#print 'gb-',guess_block,' char-',j
	if len(possible_last_bytes)!=1:
		for l in possible_last_bytes:
			for j in range(0,256):
				if check_CBC_padding_oracle(curr_block,key,change_last_bytes(prev_block,'\x02\x02',chr(j)+l)):
					guess_block = l
			#		print 'gb-',guess_block,' char-',j
	for k in range(len(curr_block)-1):
		for j in range(0,256):
			pad = len(guess_block)+1
			if check_CBC_padding_oracle(curr_block,key,change_last_bytes(prev_block,chr(pad)*pad,chr(j)+guess_block)):
				guess_block = chr(j)+guess_block
			#	print 'gb-',guess_block,' char-',j
				break
#	print guess_block
	return guess_block
			


def attack():
	#print len(ciphertext)
	plain_strings = []
	while len(plain_strings) < 10:
		ciphertext,iv = CBC_padding_oracle_encrypt(aes_key)
		num_of_blocks = len(ciphertext)/16
		prev_block = iv
		plaintext = ''
		#print num_of_blocks
		for i in range(num_of_blocks):
			#print i
			block = ciphertext[i*16:(i+1)*16]
			plaintext += break_block(block,prev_block,ciphertext[:(i)*16],aes_key,iv)
			#print plaintext
			prev_block = block
		plaintext = chal9.unpad(plaintext)
		if not plaintext in plain_strings:
			plain_strings.append(plaintext)
	return plain_strings


if __name__ == "__main__":
	aes_key = chal11.get_random_bytes(16)
	print attack()
