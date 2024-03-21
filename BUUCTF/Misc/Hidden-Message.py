s = "10110111100110101001011010001100100110101001000110011101100110101000110110011000"

flag = ''
for i in range(len(s)):
    if s[i] == '0':
        flag += '1'
    else:
        flag += '0'

print(flag)

# 原始字符串翻译
print(''.join(chr(int(s[i : i + 8], 2)) for i in range(0, len(s), 8)))
# 取反码字符串翻译
print(''.join(chr(int(flag[i : i + 8], 2)) for i in range(0, len(flag), 8)))