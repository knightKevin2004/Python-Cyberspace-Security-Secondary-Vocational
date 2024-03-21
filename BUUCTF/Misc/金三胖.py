import os                # 需要安装pillow库
from PIL import Image

img = Image.open('E:\\Learn\\Python\\BUUCTF\\Misc\\aaa.gif')
os.mkdir('E:\\Learn\\Python\\BUUCTF\\Misc\\图形拆分')      # 生成的图片的文件夹名称
try:
    i = 0
    while True:
        img.seek(i)
        img.save('E:\\Learn\\Python\\BUUCTF\\Misc\\图形拆分\\'+str(i) + '.png')   # 生成的图片名称
        i = i + 1
except:
    pass
print('共拆解图像帧数' + str(i))       # 控制台输出拆分的帧数
