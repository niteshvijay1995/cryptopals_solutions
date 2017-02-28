import requests
import time

DELAY = 0.05
sign = list('0'*40)
status_code = 500
i = 0
last_req_time = 0
time_start = time.time()
response = requests.get('http://localhost:9000/test?file=foo&signature='+''.join(sign))
last_req_time = time.time() - time_start
print last_req_time
while status_code!=200 and i < 40:
	s_flag = False
	print 'LRT - ',last_req_time
	print 'i = ',i
	for j in range(1,16):
		sign[i] = hex(j)[2:]
		time_start = time.time()
		response = requests.get('http://localhost:9000/test?file=foo&signature='+''.join(sign))
		curr_req_time = time.time() - time_start
		print '.',
		print sign[i],
		print curr_req_time
		if curr_req_time - i*DELAY*1.03 > DELAY:
			time_start = time.time()
			response = requests.get('http://localhost:9000/test?file=foo&signature='+''.join(sign))
			curr_req_time = time.time() - time_start
			print 'Rechecking - ',curr_req_time - last_req_time 
			if curr_req_time - last_req_time > DELAY*0.56:		#by hit and trial
				s_flag = True
				i += 1
				last_req_time = curr_req_time
				break
	if not s_flag:
		sign[i] = '0'
		i += 1
	print ''
	status_code = response.status_code
print 'Signature breaked - ',''.join(sign)
	