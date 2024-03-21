import os
import base64
import binascii

from numpy import binary_repr

def get_file_lists(dir_path):
    _file_list = os.listdir(dir_path)
    file_list = []
    for file_str in _file_list:
        new_dir_path = dir_path+'\\'+file_str
        if(os.path.isdir(new_dir_path)):
            file_list.extend(get_file_lists(new_dir_path))
        else:
            file_list.append(new_dir_path)
    return file_list

def important_file(path):
    FILE  =[]
    fiel_list = get_file_lists(path)
    for file in fiel_list:
        f =open(file,"r",encoding='utf-8')
        try:
            data = f.read()
            if " \t \t" in data:
                print(file)
                FILE.append(file)
        except:
            pass
    return FILE

def get_flag(f_list):
    result = ''
    for f in f_list:
        for data in open(f, 'r').readlines():
            data = data[:-1]
            if '}' in data:
                data = data.split('}')[-1]
                if '\t' in data:
                    data1 = data[::].replace('\t', '')
                    data1 = data1.replace(' ', '')
                    if not data1:
                        print([data])
                        result += data

    result = result.replace('\t', '1')
    result = result.replace(' ', '0')
    print(result)
    data = hex(int(result,2))[2:]
    data.encode('utf-8')
    str_bin = binascii.unhexlify(data)
    print(str_bin.decode('utf-8'))

if __name__ == "__main__":
    path = "绝对路径\source_code"
    FILE = important_file(path)
    get_flag(FILE)