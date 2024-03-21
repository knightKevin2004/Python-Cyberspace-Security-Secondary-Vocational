list = ['m','s',0,8,0,6,7]
del list[1]               #删除列表中的单个元素
del list                  #删除整个列表对象
list.append(8)            #列表尾部添加单个元素
L = ['m','s',0,8,0,6,7]
list.extend(L)            #在列表尾部添加列表L
demo = '.com'
list.insert(7,demo)       #在列表list的指定位置7后面添加demo元素
list.remove(0)            #在列表list中删除首次出现的元素0
list.pop()                #删除并返回列表list中下标元素，默认值为-1
list.pop(0)               #删除并返回列表list中下标为0的元素
list.count(0)             #返回列表中0元素出现的次数
list.count('m')           #返回列表中m元素出现的次数
list.reverse()            #将列表list中的所有元素逆序
list.sort(key=str,reverse=False) #key可用来指定排序依据，reverse决定是升序(False)还是降序(True)