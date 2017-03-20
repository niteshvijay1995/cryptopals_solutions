import chal10
from flask import Flask,request
import random
import json
import base64
app = Flask(__name__)
KEY = 'YELLOW_SUBMARINE'
@app.route('/transaction',methods=['GET'])
def handle_request():
	try:
		data = request.data
		data = json.loads(data)
		message = data['message']
		iv = base64.b64decode(data['iv'])
		mac = base64.b64decode(data['mac'])
		if verify_mac(message,iv,mac):
			return "Transaction Successful",200
		else:
			return "Mac doesn't match!",200
	except:
		return "Error",500

def verify_mac(msg,iv,mac):
	return mac==chal10.encrypt_CBC(msg,KEY,iv)[-16:]

if __name__ == "__main__":
	app.run(port=9000)