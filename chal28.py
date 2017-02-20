from SHA1 import SHA1

s = SHA1()
key = 'YELLOW SUBMARINE'
message = 'Hello World'
s.update(key+message)
print s.hexdigest()
