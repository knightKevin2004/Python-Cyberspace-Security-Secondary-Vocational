from collections import Counter

with open(r'E:\Learn\Python\BUUCTF\Misc\file.txt', 'r') as f:
    data = f.read()
result = Counter(data)
flag = [key for key, value in sorted(result.items(), key=lambda k: k[1], reverse=True)]
print(''.join(flag))