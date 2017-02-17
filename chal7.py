from Crypto.Cipher import AES
import base64

def decrypt_ECB(ciphertext,key):
	mode = AES.MODE_ECB
	decrypter = AES.new(key, mode)
	return decrypter.decrypt(ciphertext)

def encrypt_ECB(plaintext,key):
	mode = AES.MODE_ECB
	encrypter = AES.new(key, mode)
	return encrypter.encrypt(plaintext)

if __name__=="__main__":
	ciphertext = base64.b64decode(open('7.txt', 'r').read())
	#print ciphertext
	key = "YELLOW SUBMARINE"
	print 'Plain Text : ',decrypt_ECB(ciphertext,key)
	print 'Encryption Test : ',ciphertext == encrypt_ECB(decrypt_ECB(ciphertext,key),key)