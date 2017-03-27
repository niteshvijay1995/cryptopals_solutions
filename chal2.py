def hex_xor(a,b):
	assert len(a) == len(b)
	res = ''
	for c1,c2 in zip(a,b):
		res += "%.1x"%(int(c1,16)^int(c2,16))
	res = remove_prefix_zeros(res)
	return res

def remove_prefix_zeros(res):
	i = 0
	for x in res:
		if x == '0':
			i += 1
		else:
			break
	return res[i:]
