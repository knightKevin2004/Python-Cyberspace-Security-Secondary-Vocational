import random

def main():
    showChessboard=[['*']*hang for n in range(lie)]

def printChessboard(showChessboard):
    hang=int(input('hang:'))
    lie=int(input('lie'))
    print('+',end='')
    for rowList in showChessboard:
        print("|", end='')
        for row in rowList:
            print(" %s |" % row, end='')
        print()
        print('+',end='')
        for row in rowList:
            print("---+",end='')
        print()
    pass

if __name__ == "__main__":
    while(True):
        ifStart = int(input("1 开始，0 结束>"))
        if ifStart == 1:
            print("既然你要开始，那就放纵到底：")
            hang=int(input('hang:'))
            lie=int(input('lie'))

            printChessboard(showChessboard)
        elif ifStart == 0:
            print("Game Over!!!")
            break
        else:
            print("你再输什么，渣哥很生气，后果很严重")