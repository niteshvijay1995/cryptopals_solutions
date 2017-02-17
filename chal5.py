import binascii

def repeatingKeyXor(data,key):
	res = ''
	k = 0
	for c in data:
		res += "%.2x"%(ord(c) ^ ord(key[k]))
		k = (k+1)%3
	return res


if __name__ == "__main__":
	data = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
	KEY = b'ICE'
	expected_result = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
	result = repeatingKeyXor(data,KEY)
	print 'Encrypted data : ',result
	print 'Test Passed : ',expected_result == result