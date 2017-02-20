import chal21
import random
import time
def simulate_random():
	r = chal21.random_number()
	time.sleep(random.randint(40,100))
	r.seed_mt(int(time.time()))
	time.sleep(random.randint(40,100))
	return r.extract_number(),r.seed

def break_seed(val):
	pos_val = int(time.time())
	r = chal21.random_number()
	for seed in range(pos_val-200,pos_val):
		r.seed_mt(seed)
		if r.extract_number() == val:
			print "Seed Value : ",seed

if __name__ == "__main__":
	print 'Program running... Go grab some coffee, It will take time!'	
	a = simulate_random()
	break_seed(a[0])
	print a
