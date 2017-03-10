import chal21
import random

def untemper(y):
	y = y^(y>>18)
	y = y^(y<<15)&0xEFC60000
	y = y^(y<<7)&0x1680;
	y = y^(y<<7)&0xC4000;
	y = y^(y<<7)&0xD200000;
	y = y^(y<<7)&0x90000000;
	y = y^(y>>11)&0xFFC00000;
	y = y^(y>>11)&0x3FF800;
	y = y^(y>>11)&0x7FF;
	return y

if __name__=="__main__":
	r = chal21.random_number()
	r.seed_mt(random.randint(0,5000))
	random_numbers = []
	MT = []
	for i in range(624):
		r_no = r.extract_number()
		MT.append(untemper(r_no))
		random_numbers.append(r_no)
	r.setMT(MT)
	test_flag = True
	for i in range(624):
		r_no = r.extract_number()
		if r_no != random_numbers[i]:
			print "Test Failed - Random number doesn't match at ",i
			test_flag = False
			break
	if test_flag:
		print 'Test Passed'
