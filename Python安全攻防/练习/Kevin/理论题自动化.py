with open("理论题自动化.txt","r",encoding="utf-8") as f:
    b=1
    for line in f.readlines():
        if line.find('A',5)!=-1 and line[-3]=='A':
            print(line)