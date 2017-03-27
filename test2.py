import unittest
import random
import chal2
class Test1(unittest.TestCase):
	def test_hex_xor(self):
		hex_string1 = "1c0111001f010100061a024b53535009181c"
		hex_string2 = "686974207468652062756c6c277320657965"
		expected_string = '746865206b696420646f6e277420706c6179'
		self.assertEquals(chal2.hex_xor(hex_string1,hex_string2),expected_string)
	def test_hex_xor_with_random_inp(self):
		hex_string1 = '1'
		hex_string2 = '12'
		while len(hex_string1)!=len(hex_string2):
			int1 = random.getrandbits(200)
			int2 = random.getrandbits(200)
			hex_string1 = hex(int1)[2:].strip('L')
			hex_string2 = hex(int2)[2:].strip('L')
		expected_string = hex(int1^int2)[2:].strip('L')
		self.assertEquals(chal2.hex_xor(hex_string1,hex_string2),expected_string)

if __name__=="__main__":
	unittest.main()