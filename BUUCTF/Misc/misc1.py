import binascii

flag = "d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd"
hex_new = ''
for i in range(0, len(flag), 2):
    hex_ = flag[i:i+2]
    d_ = int('0x' + hex_, 16)
    d_surplus = d_ % 128
    temp = hex(d_surplus)[2:4]
    hex_new += temp
    f_flag = str(hex_new)
print(f_flag)


def hexStr_to_str(hex_str):
    hex = hex_str.encode('utf-8')
    str_bin = binascii.unhexlify(hex)
    return str_bin.decode('utf-8')


if __name__ == "__main__":
    hex_str = f_flag
    print(hexStr_to_str(hex_str))