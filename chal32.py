import requests
import time

DELAY = 0.005
sign = list('0'*40)
status_code = 500
i = 0
last_req_time = 0
time_start = time.time()
response = requests.get('http://localhost:9000/test?file=foo&signature='+''.join(sign))
last_req_time = time.time() - time_start
print last_req_time
while status_code!=200 and i < 40:
	print 'LRT - ',last_req_time
	print 'i = ',i
	reqs_time = [0]*16
	for k in range(10):
		for j in range(0,16):
			sign[i] = hex(j)[2:]
			time_start = time.time()
			response = requests.get('http://localhost:9000/test?file=foo&signature='+''.join(sign))
			reqs_time[j] += (time.time() - time_start)
			print '.',
	for j in range(16):
		reqs_time[j] /= 10
	curr_req_time_idx = max(range(16), key=lambda i: reqs_time[i])
	curr_req_time = reqs_time[curr_req_time_idx]
	if curr_req_time - i*DELAY*1.03 > DELAY:
	#	if curr_req_time - last_req_time > DELAY*0.56:		#by hit and trial
		sign[i] = hex(curr_req_time_idx)[2:]
		i += 1
		last_req_time = curr_req_time
		
	print ''
	status_code = response.status_code
print 'Signature breaked - ',''.join(sign)
	