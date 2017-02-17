def checkpad(s):
	rem = ord(s[len(s)-1])
	for i in range(1,rem+1):
		if ord(s[-i])!=rem:
			raise Exception('Broken Padding')
			return
	return s[:-rem]

if __name__=="__main__":
	try:
		checkpad("ICE ICE BABY\x04\x04\x04\x04")
		print 'Test Passed'
	except:
		print 'Test Failed'

	try:
		checkpad("ICE ICE BABY\x05\x05\x05\x05")
		print 'Test Failed'
	except:
		print 'Test Passed'	

	try:
		checkpad("ICE ICE BABY\x01\x02\x03\x04")
		print 'Test Failed'		
	except:
		print 'Test Passed'		
