import zipfile
import os

name = '0573'
while True:
    fz = zipfile.ZipFile(name + '.zip', 'r')
    fz.extractall(pwd=bytes(name, 'utf-8'))
    remove_name=name
    name = fz.filelist[0].filename[0:4]
    fz.close()
    os.remove('C:\\Users\\Administrator\\Desktop\\'+remove_name+".zip")