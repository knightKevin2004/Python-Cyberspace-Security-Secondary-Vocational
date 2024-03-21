import binascii

flag=binascii.unhexlify("666c61677b68656c6c6f5f776f726c647d".encode()).decode()
print(flag)