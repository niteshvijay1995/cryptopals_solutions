import chal7
import chal10
import base64
def encrypt_decrypt_CTR(text,key,nonce):
	le_nonce = int_to_little_endian(nonce,8)
	keystream = ''
	for i in range(len(text)/16+1):
		val = le_nonce+int_to_little_endian(i,8)
		keystream += chal7.encrypt_ECB(val,key)
	return chal10.xor_data(text,keystream[:len(text)])

def int_to_little_endian(num, bytes):
	r = []
	for b in range(bytes):
		r.append(chr(num%256))
		num /= 256
	return ''.join(r)

if __name__ == "__main__":
	ciphertext = base64.b64decode('L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==')
	print encrypt_decrypt_CTR(ciphertext,'YELLOW SUBMARINE',0)