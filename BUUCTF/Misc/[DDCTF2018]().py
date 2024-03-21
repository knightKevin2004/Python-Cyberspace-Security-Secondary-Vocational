# import binascii
# a="d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd"
# b=[]
# ni=0
# c=""
# for i in a:
#     if ni%2==1:
#         c=c+i
#         b.append(c)
#         c=""
#     elif ni%2==0:
#         c=c+i
#     ni+=1
# print(b)

s="d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd"
for j in range(20):
    s1 = ''
    gg=int(len(s)/2)
    for x in range(gg):
        s1 += chr((int(s[x * 2:x * 2 + 2], 16) - j) % 128)
    print(s1)