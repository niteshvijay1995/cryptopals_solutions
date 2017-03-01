import chal39

def MITM_return(data):
	pub_key,_ = chal39.genKey(200)
	cipher = chal39.rsa_encrypt(data,pub_key)
	return pub_key,cipher

def crack_rsa():
	msg = 42
	k_0,c_0 = MITM_return(msg)
	k_1,c_1 = MITM_return(msg)
	k_2,c_2 = MITM_return(msg)

	n_0 = k_0[1]
	n_1 = k_1[1]
	n_2 = k_2[1]

	m_s_0 = n_1*n_2
	m_s_1 = n_0*n_2
	m_s_2 = n_0*n_1

	N_012 = n_0*n_1*n_2

	result = (c_0*m_s_0*chal39.invmod(m_s_0,n_0)+c_1*m_s_1*chal39.invmod(m_s_1,n_1)+c_2*m_s_2*chal39.invmod(m_s_2,n_2))%N_012

	data = result**(1./3)
	print "Test Passed : ",msg==int(round(data))

if __name__=="__main__":
	crack_rsa()
