import chal18
import chal11
import chal10
import base64
import chal3
import itertools
r_strings = ['SSBoYXZlIG1ldCB0aGVtIGF0IGNsb3NlIG9mIGRheQ==',
			'Q29taW5nIHdpdGggdml2aWQgZmFjZXM=',
			'RnJvbSBjb3VudGVyIG9yIGRlc2sgYW1vbmcgZ3JleQ==',
			'RWlnaHRlZW50aC1jZW50dXJ5IGhvdXNlcy4=',
			'SSBoYXZlIHBhc3NlZCB3aXRoIGEgbm9kIG9mIHRoZSBoZWFk',
			'T3IgcG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==',
			'T3IgaGF2ZSBsaW5nZXJlZCBhd2hpbGUgYW5kIHNhaWQ=',
			'UG9saXRlIG1lYW5pbmdsZXNzIHdvcmRzLA==',
			'QW5kIHRob3VnaHQgYmVmb3JlIEkgaGFkIGRvbmU=',
			'T2YgYSBtb2NraW5nIHRhbGUgb3IgYSBnaWJl',
			'VG8gcGxlYXNlIGEgY29tcGFuaW9u',
			'QXJvdW5kIHRoZSBmaXJlIGF0IHRoZSBjbHViLA==',
			'QmVpbmcgY2VydGFpbiB0aGF0IHRoZXkgYW5kIEk=',
			'QnV0IGxpdmVkIHdoZXJlIG1vdGxleSBpcyB3b3JuOg==',
			'QWxsIGNoYW5nZWQsIGNoYW5nZWQgdXR0ZXJseTo=',
			'QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=',
			'VGhhdCB3b21hbidzIGRheXMgd2VyZSBzcGVudA==',
			'SW4gaWdub3JhbnQgZ29vZCB3aWxsLA==',
			'SGVyIG5pZ2h0cyBpbiBhcmd1bWVudA==',
			'VW50aWwgaGVyIHZvaWNlIGdyZXcgc2hyaWxsLg==',
			'V2hhdCB2b2ljZSBtb3JlIHN3ZWV0IHRoYW4gaGVycw==',
			'V2hlbiB5b3VuZyBhbmQgYmVhdXRpZnVsLA==',
			'U2hlIHJvZGUgdG8gaGFycmllcnM/',
			'VGhpcyBtYW4gaGFkIGtlcHQgYSBzY2hvb2w=',
			'QW5kIHJvZGUgb3VyIHdpbmdlZCBob3JzZS4=',
			'VGhpcyBvdGhlciBoaXMgaGVscGVyIGFuZCBmcmllbmQ=',
			'V2FzIGNvbWluZyBpbnRvIGhpcyBmb3JjZTs=',
			'SGUgbWlnaHQgaGF2ZSB3b24gZmFtZSBpbiB0aGUgZW5kLA==',
			'U28gc2Vuc2l0aXZlIGhpcyBuYXR1cmUgc2VlbWVkLA==',
			'U28gZGFyaW5nIGFuZCBzd2VldCBoaXMgdGhvdWdodC4=',
			'VGhpcyBvdGhlciBtYW4gSSBoYWQgZHJlYW1lZA==',
			'QSBkcnVua2VuLCB2YWluLWdsb3Jpb3VzIGxvdXQu',
			'SGUgaGFkIGRvbmUgbW9zdCBiaXR0ZXIgd3Jvbmc=',
			'VG8gc29tZSB3aG8gYXJlIG5lYXIgbXkgaGVhcnQs',
			'WWV0IEkgbnVtYmVyIGhpbSBpbiB0aGUgc29uZzs=',
			'SGUsIHRvbywgaGFzIHJlc2lnbmVkIGhpcyBwYXJ0',
			'SW4gdGhlIGNhc3VhbCBjb21lZHk7',
			'SGUsIHRvbywgaGFzIGJlZW4gY2hhbmdlZCBpbiBoaXMgdHVybiw=',
			'VHJhbnNmb3JtZWQgdXR0ZXJseTo=',
			'QSB0ZXJyaWJsZSBiZWF1dHkgaXMgYm9ybi4=']

def break_CTR():
	aes_key = chal11.get_random_bytes(16)
	nonce = 0
	ciphertexts = []
	strings = []
	file = open('20.txt','r')
	for line in file:
		strings.append(line)
	#print strings
	for plaintext in strings:
		plaintext = base64.b64decode(plaintext)
		#print plaintext
		ciphertexts.append(chal18.encrypt_decrypt_CTR(plaintext,aes_key,nonce))

	transpose_cipher = map(None,*ciphertexts)

	keystream = ''
	for ele in transpose_cipher:
		data = ''.join(filter(None,ele))
		keystream += chr(chal3.breakSingleByteXOR(data)[0])

	for ele in ciphertexts:
		#print len(ele)
		print chal10.xor_data(ele,keystream[:len(ele)])



if __name__=="__main__":
	break_CTR()





