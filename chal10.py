import chal7
import chal9
from binascii import b2a_hex,a2b_base64
import base64
BLOCK_SIZE = 16
def xor_data(A, B):
  return ''.join(chr(ord(A[i])^ord(B[i])) for i in range(len(A)))
def encrypt_CBC(plaintext,key,iv):
	ciphertext = ''
	last_cipher = iv
	plaintext = chal9.pad(plaintext,16)
	for i in range(len(plaintext)/BLOCK_SIZE):
		plain_block = plaintext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE]
		plain_block = xor_data(plain_block,last_cipher)
		last_cipher = chal7.encrypt_ECB(plain_block,key)
		ciphertext += last_cipher
	return ciphertext
def decrypt_CBC(ciphertext,key,iv):
	plaintext = ''
	last_cipher = iv
	for i in range(len(ciphertext)/BLOCK_SIZE):
		plain_block = chal7.decrypt_ECB(ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE],key)
		plain_block = xor_data(plain_block,last_cipher)
		last_cipher = ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE]
		plaintext += plain_block
	return chal9.unpad(plaintext)

if __name__=="__main__":
	cipher = base64.b64decode(open("10.txt",'r').read())
	print decrypt_CBC(cipher,"YELLOW SUBMARINE",'\x00'*16)
