import hashlib
import chal39
import time
import json
from flask import Flask,request
app = Flask(__name__)
pub_key = None
priv_key = None
hash_table = {}

@app.route('/rsa_decrypt',methods=['GET'])
def handle_request():
	if 'cipher' in request.args:
		cipher = int(request.args['cipher'])
	else:
		return 'Error - Cipher not found',500
	hash = hashlib.sha1(str(cipher)).hexdigest()
	if hash in hash_table:
		return 'Cipher already decrypted at '+str(hash_table[hash]),300
	hash_table[hash] = int(time.time())
	return str(chal39.rsa_decrypt(cipher,priv_key)),200


@app.route('/get_key',methods=['GET'])
def get_public_key():
	response = {}
	response['e'] = pub_key[0]
	response['n'] = pub_key[1]
	return json.dumps(response)

if __name__ == "__main__":
	pub_key,priv_key = chal39.genKey(100)
	app.run(port=9000)