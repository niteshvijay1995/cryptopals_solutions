import hashlib
import chal39

y = 0x2d026f4bf30195ede3a088da85e398ef869611d0f68f0713d51c9c1a3a26c95105d915e2d8cdf26d056b86b8a7b85519b1c23cc3ecdc6062650462e3063bd179c2a6581519f674a61f1d89a1fff27171ebc1b93d4dc57bceb7ae2430f98a6a4d83d8279ee65d71c1203d2c96d65ebbf7cce9d32971c3de5084cce04a2e147821
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
def same_value_in_list(r):
	for i in range(len(r)):
		for j in range(i+1,len(r)):
			if r[i]==r[j]:
				return i,j


def find_k(m1,m2,s1,s2,q):
	return ((m1-m2)%q * chal39.invmod(s1-s2,q))%q

if __name__=="__main__":
	file = open('44.txt','r').readlines()
	msgs = []
	r = []
	s = []
	m = []
	for i in range(0,len(file)/4):
		msgs.append(file[i*4].strip().split(':')[1])
		s.append(file[i*4+1].strip().split(':')[1])
		r.append(file[i*4+2].strip().split(':')[1])
		m.append(file[i*4+3].strip().split(':')[1])

	i,j = same_value_in_list(r)
	print "Same value in list function test - ",r[i]==r[j]
	k = find_k(int(m[i],16),int(m[j],16),int(s[i]),int(s[j]),q)
	x = (((int(s[i])*k) - int(m[i],16))%q * chal39.invmod(int(r[i]),q))%q
	print "Private key Cracked :)"
	print "Key Check - ",hashlib.sha1(hex(x)[2:-1]).hexdigest()=="ca8f6f7c66fa362d40760d135b763eb8527d3d52"
