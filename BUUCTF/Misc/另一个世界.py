a=[0b01101011,0b01101111,0b01100101,0b01101011,0b01101010,0b00110011,0b01110011]
flag=""
for i in a:
    flag+=chr(i)
print("flag{"+flag+"}")