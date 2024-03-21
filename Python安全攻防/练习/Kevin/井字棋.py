import random

def main():
    boardList = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
    while(True):
        printBoard(boardList)
        player(boardList)
        printBoard(boardList)
        if winManager(boardList):
            break
        computer(boardList)
        printBoard(boardList)
        if winManager(boardList):
            break
        pass
    pass

def winManager(boardList):
    res = ifWin(boardList)
    if res == "X":
        print("玩家赢了")
        return True
    elif res == "O":
        print("电脑赢了")
        return True
    elif res == "Q":
        print("平局")
        return True
    return False

def printBoard(boardList):
    for rowList in boardList:
        print("|", end='')
        for row in rowList:
            print(" %s |" % row, end='')
        print()
        print('+',end='')
        for row in rowList:
            print("---+",end='')
        print()
    pass

def player(boardList):
    while(True):
        pos = list(map(int,(input("请你下棋 1,1>")).split(',')))
        res = setChess(boardList, pos[0]-1, pos[1]-1, "X")
        if not res:
            print("下棋错误 请重新下")
            printBoard(boardList)
        else:
            break

def computer(boardList):
    while(True):
        res = setChess(boardList, random.randint(0,2), random.randint(0,2), "O")
        if res:
            break

def setChess(boardList, x, y, types):
    ret = boardList[x][y]
    if ret == ' ':
        boardList[x][y] = types
        return True
    else:
        return False

def ifWin(boardList):
    # 平局：Q
    # 继续：C
    # 横线
    for rowList in boardList:
        if rowList[0] == rowList[1] and rowList[1] == rowList[2] and rowList[2] != ' ':
            return rowList[0]
    # 竖线
    boardLenth = len(boardList)
    for row in range(boardLenth):
        if boardList[row][0] == boardList[row][1] and boardList[row][1] == boardList[row][2] and boardList[row][2] != ' ':
            return boardList[rowList][1]
    # xie 1

    """
    for rowList in boardList:
        clock = True
        for row in rowList:
            if row != types:
                clock = False
                break
        if clock:
            print("Win 1")
            return types

    boardLenth = len(boardList)
    boardColList = len(boardList[0])
    for x in range(0,boardLenth):
        clock = True
        for y in range(0,boardColList):
            if boardList[y][x] != types:
                clock = False
                break
        if clock:
            print("Win 2")
            return types
    
    clock = True
    for i in range(boardLenth):
        if boardList[i][i] != types:
            clock = False
            break
    if clock:
        print("Win 3")
        return types
    """
    if boardList[0][0] == boardList[1][1] and boardList[1][1] == boardList[2][2] and boardList[2][2] != ' ':
        return boardList[2][2]

    if boardList[0][2] == boardList[1][1] and boardList[1][1] == boardList[2][0] and boardList[2][0] != ' ':
        return boardList[0][2]

    # 平局
    for rowList in boardList:
        for row in rowList:
            if row == ' ':
                return "C"
    return "Q"
    print(x,y)

if __name__ == "__main__":
    while(True):
        ifStart = int(input("1 开始，0 结束>"))
        if ifStart:
            print("游戏开始：")
            main()
        elif ifStart == 0:
            print("游戏结束")
            break
        else:
            print("重新输入")