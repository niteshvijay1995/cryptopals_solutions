import chal3
import binascii
from Crypto.Util.strxor import strxor_c

def break_singl_char_xor():
	filename = '4.txt'
	max_score = 0
	max_score_key = ''
	f=open(filename,'r')
	plain_string = ''
	for line in f:
		if line[-1]=='\n':
			line = line[:-1]
		#print line
		s = binascii.unhexlify(line)
		res = chal3.breakSingleByteXOR(s)
		#print res
		sc = chal3.score(res[1])
		if sc>max_score:
			max_score_key = res[0]
			max_score = sc
			plain_string = res[1]
	print plain_string
	f.close()

if __name__ == "__main__":
	break_singl_char_xor()