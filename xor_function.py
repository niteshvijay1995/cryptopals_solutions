def xor(a,b):
	assert len(a) == len(b)
	print hex(int(a,16) ^ int(b,16))

if __name__ == "__main__":
	xor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")

