import base64
import chal3
from Crypto.Util.strxor import strxor_c
from binascii import b2a_hex, a2b_hex
import base64
import itertools

def decryptRepeatingKeyXor(s, key):
	length = len(s)
	key = key*(length/len(key)+1)
	key = key[0:length]
	#print length,"==",len(key)
	ret = ("%x" % (int(b2a_hex(s),16)^int(b2a_hex(key),16)))
	return a2b_hex(ret)


def hamming_dist(a,b):
	ed = 0
	for c1,c2 in zip(a,b):
		#print c1,c2
		b1 = format(ord(c1),'b')
		b2 = format(ord(c2),'b')
		if len(b1)!=7:
			b1 = ('0'*(7-len(b1)))+b1
		if len(b2)!=7:
			b2 = ('0'*(7-len(b2)))+b2
		for bit1,bit2 in zip(b1,b2):
			if bit1 != bit2:
				ed += 1
		#print ed
	return ed 

def breakRepeatingKeyXor(x, k):
    blocks = [x[i:i+k] for i in range(0, len(x), k)]
    transposedBlocks = list(zip_longest(*blocks, fillvalue=0))
    key = [chal3.breakSingleByteXOR(bytes(x))[0] for x in transposedBlocks]
    return bytes(key)

def normalizedEditDistance(x, k):
	blocks = []
	for i in range(0,len(x),k):
		blocks.append(x[i:i+k])
	pairs = list(itertools.combinations(blocks[0:4], 2))
	scores = [hamming_dist(p[0], p[1])/float(k) for p in pairs]
	return sum(scores) / len(scores)


if __name__ == "__main__":
	#Test Hammin distance function
	if hamming_dist("this is a test","wokka wokka!!!") == 37:
		print "SUCCESS : hamming_dist function test passed"
	else:
		print "FAILED : hamming_dist function test failed"

	print "\n--------------------------------------------\n"

	#File operations
	filename = "6.txt"
	f = open(filename,'r')
	cipher = ''
	for line in f:
		cipher += line
	cipher = base64.b64decode(cipher)

	MAX_KEY_SIZE = 80
	normKeySize = float('inf')
	key_length = 0
	for k in range(2,MAX_KEY_SIZE):
		curr_norm = normalizedEditDistance(cipher,k)
		#print curr_norm
		if normKeySize > curr_norm:
			normKeySize = curr_norm
			key_length = k
	print "Key Length : ",key_length

	key =''

	for x in range(1,key_length+1):
		c_to_break = ''
		for i in range(len(cipher)/key_length):
			c_to_break += cipher[(key_length*i)+x-1]
		res = chal3.breakSingleByteXOR(c_to_break)
		key += chr(res[0])
	print "Key : ", key
	print "\n======================= Decrypted Text ================================\n"
	print decryptRepeatingKeyXor(cipher,key)
