x = 2
for i in range(19260816):
    x = x * 10 + 2
    x %= (1e9 + 7)
print(x)