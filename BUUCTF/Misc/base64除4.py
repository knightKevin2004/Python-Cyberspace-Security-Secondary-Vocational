import base64

print(base64.b16decode("666C61677B45333342374644384133423834314341393639394544444241323442363041417D").decode())



import binascii

def hexStr_to_str(hex_str):
    hex = hex_str.encode('utf-8')
    str_bin = binascii.unhexlify(hex)
    return str_bin.decode('utf-8')

if __name__ == "__main__":
	hex_str = '666C61677B45333342374644384133423834314341393639394544444241323442363041417D' 
	print(hexStr_to_str(hex_str))