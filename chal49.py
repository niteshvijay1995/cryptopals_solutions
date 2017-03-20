import requests
import chal10
import chal11
import json
import base64

def attack(data):
	iv = base64.b64decode(data['iv'])
	msg = data['message']
	msg_length = len(msg)
	blocks = msg_length/len(iv)
	print msg[blocks-1*16:]
	iv = iv[:-3]+chr(ord(iv[-3])^ord('5')^ord('9'))+iv[-2:]
	data['iv'] = base64.b64encode(iv)
	msg = msg[:-3]+'9'+msg[-2:]
	data['message'] = msg
	response = requests.get('http://localhost:9000/transaction',data=json.dumps(data))
	print 'Attacker Test#1 - ',response.content=="Transaction Successful"

KEY = 'YELLOW_SUBMARINE'
iv = chal11.get_random_bytes(16)
msg = 'from=Target&to=Nitesh&amount=500'
mac = chal10.encrypt_CBC(msg,KEY,iv)[-16:]
data = {}
data['message'] = msg
data['iv'] = base64.b64encode(iv)
data['mac'] = base64.b64encode(mac)
response = requests.get('http://localhost:9000/transaction',data=json.dumps(data))
print 'Server Test#1 - ',response.content=="Transaction Successful"
attack(data)
data['message'] = 'from=Target&to=Nitesh&amount=5000'
response = requests.get('http://localhost:9000/transaction',data=json.dumps(data))
print 'Server Test#2 - ',response.content=="Mac doesn't match!"


