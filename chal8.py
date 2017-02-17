def check_ECB(ciphertext):
	BLOCK_SIZE  = 16
	length = len(ciphertext)
	blocks = length/BLOCK_SIZE
	for i in range(blocks):
		for j in range(i+1,blocks):
			if ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE] == ciphertext[j*BLOCK_SIZE:(j+1)*BLOCK_SIZE]:
				return True
	return False

if __name__ == "__main__":
	file = open("8.txt")
	lineno = 1
	for line in file:
		if check_ECB(line):
			print 'ECB encrypted ciphertext detected at line number : ',lineno
		lineno += 1
