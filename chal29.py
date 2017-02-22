from SHA1 import SHA1


def verify_SHA1(key,message,hash):
	s = SHA1()
	s.update(key+message)
	return hash == s.hexdigest()

def padding(stream):
		l = len(stream)  # Bytes
		hl = [int((hex(l*8)[2:]).rjust(16, '0')[i:i+2], 16)
			for i in range(0, 16, 2)]

		l0 = (56 - l) % 64
		if not l0:
			l0 = 64

		if isinstance(stream, str):
		stream += chr(0b10000000)
		stream += chr(0)*(l0-1)
		for a in hl:
			stream += chr(a)
		elif isinstance(stream, bytes):
			stream += bytes([0b10000000])
			stream += bytes(l0-1)
			stream += bytes(hl)

		return stream