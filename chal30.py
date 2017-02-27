from MD4 import MD4
import binascii
import random
import chal11
from struct import pack, unpack

KEY = ''

def verify_MD4(msg, sig):
		m = MD4()
		m.update(KEY+msg)
		return m.hexdigest() == sig

def pad(msg,n=None):
	if n==None:
		n = len(msg)
	bit_len = n * 8
	index = (bit_len >> 3) & 0x3fL
	pad_len = 120 - index
	if index < 56:
		pad_len = 56 - index
	padding = '\x80' + '\x00'*63
	padded_msg = msg + padding[:pad_len] + pack('<Q', bit_len)
	return padded_msg


def break_hash_append(data,hash,suffix,max_key_len):
	for i in range(max_key_len):
		mod_data = pad(data,len(data)+i)
		md4 = MD4(int(hash[0:8],16),int(hash[8:16],16),int(hash[16:24],16),int(hash[24:32],16),len(suffix)+len(mod_data)+i)
		md4.update(suffix)
		if verify_MD4(mod_data+suffix,md4.hexdigest()):
			print 'Yeahh! Hash Cracked :)\nHASH -',md4.digest()
			return

if __name__ == "__main__":
	KEY = chal11.get_random_bytes(random.randint(1,100))
	data = "comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
	md4 = MD4()
	md4.update(KEY+data)
	hash = md4.hexdigest()
	#print verify_SHA1(data,hash)
	break_hash_append(data,hash,";admin=true",100)



'''
Problem faced by me :
Earlier I was using digest() method instead of hexdigest() method and that creates the problem because to break the hash I need to update the constants value in implementation and digest method doesnot give justified hex value i.e. it does not append any zeroes to make the complete length 32.
So it created the problem at line number 30 where values are hardcoded. 

It took me a day to figure out the problem in the code.

'''