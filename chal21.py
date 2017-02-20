class random_number:
	W = 32
	N = 624
	M = 397
	R = 31
	A = 0x9908B0DF
	U = 11
	D = 0xFFFFFFFF
	S = 7
	B = 0x9D2C5680
	T = 15
	C = 0xEFC60000
	L = 18
	F = 1812433253
	MT = [0]*N
	index = N+1
	LOWER_MASK = (1<<R)-1
	UPPER_MASK = 0
	seed = 0

	def _init_(self):
		self.UPPER_MASK = self.get_lower_x_bits(~LOWER_MASK,W)

	def get_lower_x_bits(self,val,x):
		mask = pow(2,x)-1
		return val&mask

	def seed_mt(self,seed):
		self.index = self.N
		self.MT[0] = seed
		self.seed = seed
		for i in range(1,self.N-1):
			self.MT[i] = self.get_lower_x_bits(self.F*(self.MT[i-1] ^ (self.MT[i-1] >> (self.W-2)))+i,self.W)


	def extract_number(self):
		if self.index >= self.N:
			if self.index > self.N:
				print 'ERROR'

			self.twist()
		y = self.MT[self.index]
		y = y ^ ((y >> self.U) & self.D)
		y = y ^ ((y << self.S) & self.B)
		y = y ^ ((y << self.T) & self.C)
		y = y ^ (y >> 1)

		self.index = self.index + 1
		return self.get_lower_x_bits(y,self.W)

	def twist(self):
		for i in range(self.N-1):
			x = (self.MT[i] & self.UPPER_MASK) + (self.MT[(i+1)%self.N] & self.LOWER_MASK)
			xA = x >> 1
			if x%2 != 0:
				xA = xA ^ self.A

			self.MT[i] = self.MT[(i+self.M)%self.N] ^ xA
		self.index = 0

	def untemper(y):
		y = y ^ (y << 1)
		



if __name__ == "__main__":
	r = random_number()
	r.seed_mt(1)
	print r.extract_number()
	print r.extract_number()

