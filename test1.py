import unittest
import chal1
class Test1(unittest.TestCase):
	def test_hex_to_base64(self):
		hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
		expected_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
		self.assertEquals(chal1.hex_to_base64(hex_string),expected_string)

if __name__=="__main__":
	unittest.main()