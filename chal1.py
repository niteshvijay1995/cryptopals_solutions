
def hex_to_base64(hex_string):
	return hex_string.decode("hex").encode("base64").strip()
