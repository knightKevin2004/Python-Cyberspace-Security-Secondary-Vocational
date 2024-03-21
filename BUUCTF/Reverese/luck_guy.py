f1="GXY{do_not_"
f2="icug`ofF7x\\'"
for i in range(8):
    if i%2==1:
        ord(f2[i])-=2
    else:
        f2[i]-=1
print(f2)