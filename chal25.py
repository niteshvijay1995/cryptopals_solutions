import base64
import chal21
import chal7
import chal18
import chal11
import chal10
#def edit(ciphertext,key,offset,newtext):
KEY = ''
nonce = 0
def decrypt_file():
	ciphertext = base64.b64decode(open('25.txt', 'r').read())
	#print ciphertext
	key = "YELLOW SUBMARINE"
	return chal7.decrypt_ECB(ciphertext,key)

def edit(ciphertext,offset,newtext):
	plaintext = chal18.encrypt_decrypt_CTR(ciphertext,KEY,nonce)
	mod_plaintext = plaintext[:offset]+newtext+plaintext[offset+len(newtext):]
	print mod_plaintext
	print len(mod_plaintext)
	return chal18.encrypt_decrypt_CTR(mod_plaintext,KEY,nonce)

#def break_CTR():


if __name__=="__main__":
	plaintext = decrypt_file()	
	print plaintext
	KEY = chal11.get_random_bytes(16)
	nonce = 0
	ciphertext = chal18.encrypt_decrypt_CTR(plaintext,KEY,nonce)
	#print ciphertext
	new_ciphertext = edit(ciphertext,0,'A'*len(ciphertext))
	k = chal10.xor_data(new_ciphertext,'A'*len(ciphertext))
	print chal10.xor_data(k,ciphertext)
