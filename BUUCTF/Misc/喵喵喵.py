#Author: mochu7
def decode(arg1):
	ciphertext = arg1[::-1]
	flag = ''
	for i in range(len(ciphertext)):
		if i % 2 == 0:
			s = int(ciphertext[i]) - 10
		else:
			s = int(ciphertext[i]) + 10 
		s = s ^ i
		flag += chr(s)
	print(flag)

if __name__ == '__main__':
	ciphertext = [
    '96',
    '65',
    '93',
    '123',
    '91',
    '97',
    '22',
    '93',
    '70',
    '102',
    '94',
    '132',
    '46',
    '112',
    '64',
    '97',
    '88',
    '80',
    '82',
    '137',
    '90',
    '109',
    '99',
    '112']
	decode(ciphertext)