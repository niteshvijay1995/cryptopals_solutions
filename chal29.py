from SHA1 import SHA1
import binascii
import random
import chal11


KEY = ''

def verify_SHA1(message,hash):
	s = SHA1()
	s.update(KEY+message)
	return hash == s.hexdigest()

def pad(stream,l=None):
		if l==None:
			l = len(stream)  # Bytes
		hl = [int((hex(l*8)[2:]).rjust(16, '0')[i:i+2], 16)
			for i in range(0, 16, 2)]

		l0 = (56 - l) % 64
		if not l0:
			l0 = 64

		if isinstance(stream, str):
			stream += chr(0b10000000)
			stream += chr(0)*(l0-1)
			for a in hl:
				stream += chr(a)
		elif isinstance(stream, bytes):
			stream += bytes([0b10000000])
			stream += bytes(l0-1)
			stream += bytes(hl)
		return stream


def break_hash_append(data,hash,suffix,max_key_len):
	for i in range(max_key_len):
		mod_data = pad(data,len(data)+i)
		sha2 = SHA1(int(hash[0:8],16),int(hash[8:16],16),int(hash[16:24],16),int(hash[24:32],16),int(hash[32:40],16),len(suffix)+len(mod_data)+i)
		sha2.update(suffix)
		if verify_SHA1(mod_data+suffix,sha2.hexdigest()):
			print 'Yeahh! Hash Cracked :)\nHASH -',sha2.hexdigest()
			return
if __name__ == "__main__":
	KEY = chal11.get_random_bytes(random.randint(1,100))
	data = "comment1=cooking%20MCs;userdata=foo;comment2=%20like%20a%20pound%20of%20bacon"
	sha = SHA1()
	sha.update(KEY+data)
	hash = sha.hexdigest()
	#print verify_SHA1(data,hash)
	break_hash_append(data,hash,";admin=true",100)
