import chal7
import chal9
import chal11

key = ''
def profile_for(email):
	user_id = 10
	email = email.replace('&','')
	email = email.replace('=','')
	profile_dict = {}
	profile_dict['email'] = email
	profile_dict['uid'] = user_id
	user_id += 1
	profile_dict['role'] = 'user'
	ret_str = 'email='+email+'&uid='+str(user_id)+'&role=user'
	return encrypt(ret_str,key)

def encrypt(plaintext,key):
	plaintext = chal9.pad(plaintext,16)
	return chal7.encrypt_ECB(plaintext,key)

def decrypt(ciphertext,key):
	plaintext = chal7.decrypt_ECB(ciphertext,key)
	return chal9.unpad(plaintext)

def break_cipher():
	c1 = profile_for('qwe@ty.yu')
	c2 = profile_for('qwer@ty.yuadmin')
	c3 = profile_for('qwert33@ty.yu')
	c4 = profile_for('qwer@ty.yu')
	c = c4[:16]+c3[16:32]+c2[16:32]+c1[32:48]
	#print len(c)
	print decrypt(c,key)

if __name__=="__main__":
	key = chal11.get_random_bytes(16)
	#print profile_for("abc@xyz.com")
	break_cipher()
