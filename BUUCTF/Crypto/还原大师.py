import hashlib
a="TASC?O3RJMV?WDJKX?ZM"
for i in range(26):
    b=a.replace("?",chr(i+65),1)
    for j in range(26):
        c=b.replace("?",chr(j+65),1)
        for z in range(26):
            flag=c.replace("?",chr(z+65),1)
            mdf=hashlib.md5()
            mdf.update(flag.encode())
            flag=mdf.hexdigest().upper()
            if flag[:4]=="E903":
                print(flag)