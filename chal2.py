def hex_xor(a,b):
	assert len(a) == len(b)
	res = ''
	for c1,c2 in zip(a,b):
		res += "%.1x"%(int(c1,16)^int(c2,16))
	return res

if __name__ == "__main__":
	print "Test#1 : ","746865206b696420646f6e277420706c6179"==hex_xor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965")

