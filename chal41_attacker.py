import json
import requests
import chal39
import random

org_plain_text = random.randint(0,10000)
response = requests.get("http://localhost:9000/get_key")
pub_key_json = json.loads(response.content)
pub_key = [pub_key_json['e'],pub_key_json['n']]
cipher = chal39.rsa_encrypt(org_plain_text,pub_key)
dec_plain_text = requests.get("http://localhost:9000/rsa_decrypt?cipher="+str(cipher))
print "Server decryption test : ",dec_plain_text.status_code == 200 and org_plain_text==int(dec_plain_text.content)
print "Server hash validation test : ",requests.get("http://localhost:9000/rsa_decrypt?cipher="+str(cipher)).status_code == 300

N = pub_key[1]
E = pub_key[0]
S = random.randint(2,N)
C1 = (pow(S,E,N)*cipher)%N

response = requests.get("http://localhost:9000/rsa_decrypt?cipher="+str(C1))
if response.status_code == 200:
	cracked_plain_text = (int(response.content)%N * chal39.invmod(S,N))%N
	print "Cracked Plain Text : ",cracked_plain_text
	print "Attacker decryption test : ",cracked_plain_text==org_plain_text