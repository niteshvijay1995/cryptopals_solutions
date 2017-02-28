from SHA1 import SHA1
import chal10
import chal11
import time
from flask import Flask,request
import random
app = Flask(__name__)
DELAY = 0.005
KEY = ''
@app.route('/test',methods=['GET'])
def handle_request():
	if 'file' in request.args:
		file = request.args['file']
	else:
		return 'Error - File not found',500
	if 'signature' in request.args:
		signature = request.args['signature']
	else:
		return 'Error - Signature not found',500
	if insecure_compare(signature,hmac_sha1(KEY,file.encode('ascii'))):
		return 'True',200
	else:
		return 'False',500


BLOCK_SIZE = 40
def hmac_sha1(key,message):
	hash = SHA1()
	if len(key)>BLOCK_SIZE:
		hash.update(key)
		key = hash.hexdigest()
	if len(key) < BLOCK_SIZE:
		key = key + '\x00'*(BLOCK_SIZE-len(key))

	o_key_pad = chal10.xor_data(chr(0x5c)*BLOCK_SIZE,key)
	i_key_pad = chal10.xor_data(chr(0x36)*BLOCK_SIZE,key)

	hash1 = SHA1()
	hash1.update(i_key_pad + message)
	hash2 = SHA1()
	hash2.update(o_key_pad + hash1.hexdigest())
	return hash2.hexdigest()

def insecure_compare(A,B):
	print A
	print B
	if len(A)!=len(B):
		return False
	for a,b in zip(A,B):
		if a!=b:
			return False
		time.sleep(DELAY)
	return True

if __name__ == "__main__":
	KEY = chal11.get_random_bytes(random.randint(1,100))
	app.run(port=9000)