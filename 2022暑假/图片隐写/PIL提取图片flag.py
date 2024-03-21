#-*- coding : utf-8 -*-
# coding: utf-8

from PIL import Image
import os

a=Image.open("E:\\Learn\\Python\\2022暑假\\图片隐写\\glance.gif")
path=("E:\\Learn\\Python\\2022暑假\\图片隐写\\拆开图片\\")
#os.mkdir(path)

try:
    i = 0
    while True:
        a.seek(i)
        a.save(path+str(i)+'.png')
        i = i +1
except:
    pass
print('共拆解图像帧数'+str(i))