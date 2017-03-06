
import chal39
import hashlib
import binascii
import re
import math
def get_signature(msg,priv_key):
	msg_hash = hashlib.sha1(msg).hexdigest()
	padded_msg = b'\x00\x01' + (b'\xff')*(128 - len(msg_hash) - 3) +'\x00' + msg_hash
	return chal39.rsa_decrypt(chal39.str_to_num(padded_msg),priv_key)

def verify_signature(signature,msg,pub_key):
	msg_hash = hashlib.sha1(msg).hexdigest()
	padded_msg = b'\x00'+chal39.num_to_str(chal39.rsa_encrypt(signature,pub_key))
	padded_msg = re.compile(b'\x00\x01\xff+?\x00(.{40})',re.DOTALL).split(padded_msg)
	return msg_hash == padded_msg[1]

def forge_signature(pub_key,msg):
	n = pub_key[1]
	msg_hash = hashlib.sha1(msg).hexdigest()
	padded_msg = b'\x00\x01\xff\x00'+msg_hash+b'\x00'*(128-len(msg_hash)-3)
	msg_num = chal39.str_to_num(padded_msg)
	sign = iroot(3,msg_num)+1
	return sign


def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

if __name__=="__main__":
	msg = "hi mom"
	pub_key,priv_key = chal39.genKey(1024)
	signature = get_signature(msg,priv_key)
	print 'Signature verification test : ',verify_signature(signature,msg,pub_key)
	forged_signature = forge_signature(pub_key,msg)
	print 'Forged Signature Test :',verify_signature(forged_signature,msg,pub_key)