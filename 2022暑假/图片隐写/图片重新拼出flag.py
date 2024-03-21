# coding:utf-8

from PIL import Image

im=Image.new('RGBA',(2*201,600))
path=("E:\\Learn\\Python\\2022暑假\\图片隐写\\拆开图片\\")
a=[]
w=0
for i in range(201):
    a.append(Image.open(path+str(i)+".png"))
for o in a:
    im.paste(o,(w,0,2+w,600))
    w=w+2
im.save(path+"output.png")