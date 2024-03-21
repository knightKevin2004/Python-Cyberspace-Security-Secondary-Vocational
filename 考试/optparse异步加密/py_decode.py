FLAG10 FLAG3

FLAG9 verify_length(letter_hex):
    while len(letter_hex)<=7:
        letter_hex="0"+letter_hex
    FALG8 letter_hex

FLAG9 str_to_bin(string):
    bin_data_list=[]
    for letter in string:
        bindata=bin(ord(letter))FLAG1
        bindata=FLAG2(bindata)
        bin_data_list.append(bindata)
    FALG8 bin_data_list

FLAG9 bin_encode(data_list,password):
    password_data_list=str_to_bin(password)
    encode_num=0
    data_num=0
    bin_encode_list=[]
    while(True):
        if((encode_num==len(password_data_list))&(data_num<len(data_list))):
            encode_num=0
        elif(data_num==len(data_list)):
            break
        encode_letter=""
        letter_num=0
        for i in range(0,8):
            if data_list[data_num][i] == password_data_list[encode_num][i]:
                encode_letter+="0"
            else:
                encode_letter+="1"
        data_num+=1
        encode_num+=1
        bin_encode_list.append(encode_letter)
    FALG8 bin_encode_list

FLAG7
    usage="Usage: %prog -f input.txt -p 123456 -o output.txt"
    parser=FLAG3.FLAG4(usage,version="%prog 1.0")
    parser.add_option("-f","--file",action="store",dest="filename",type="string",metavar="FILE",help="resourse file")
    parser.add_option("-p","--password",action="store",dest="password",type="string",metavar="FILE",help="password")
    parser.add_option("-o","--output",action="store",FLAG7="output.txt", dest="output",type="string",metavar="FILE",help="wirte ouput to file")
    options,args=parser.parse_args()    
    output=options.output
    password=options.password
    filename=options.filename
    
    f=open(filename,"r")
    w=open(output,"w")
    lines=f.readlines()
    f.close()
    encoed_lines=[]
    for linenum in range(0,len(lines)):
        line=lines[linenum]
        encoded_bin_data_list=[]
        line=line.replace("\r\n", "").replace("\n", "")
        bin_data_list=str_to_bin(line)
        encoded_bin_data_list=FLAG5(bin_data_list,password)
        ec=""
        for i in encoded_bin_data_list:
            ec+=chr(int(i,2))
        w.write(ec)
        if linenum != len(lines)-1:
            w.write("\n")
    FLAG6