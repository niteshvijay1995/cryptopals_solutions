#Nitesh Vijay
#Set2

def pad(s,block_size):
	final_len = (len(s)/block_size+1)*block_size
	rem = final_len-len(s)
	string_to_add = chr(rem)*rem
	return s + string_to_add

def unpad(s):
	rem = ord(s[len(s)-1])
	for i in range(1,rem+1):
		if ord(s[-i])!=rem:
			raise Exception('Broken Padding')
			return
	return s[:-rem]

if __name__=="__main__":
	#test
	print pad("YELLOW SUBMARINE",20)
	print "Pad Test : ",pad("YELLOW SUBMARINE",20)=="YELLOW SUBMARINE\x04\x04\x04\x04"
