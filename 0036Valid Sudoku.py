def isValidSudoku(board: list[list[str]]) -> bool:

    # 直排不能有重複的
    for i in range(len(board)):
        temp = [] # 儲存相同數據用
        for j in range(len(board[i])):
            if board[i][j] != ".":
                temp.append(board[i][j])
        if len(list(set(temp))) != len(temp):
            return False
    # 橫排不能有重複的
    for i in range(len(board)):
        temp = [] # 儲存相同數據用
        for j in range(len(board[i])):
            if board[j][i] != ".":
                temp.append(board[j][i])
        if len(list(set(temp))) != len(temp):
            return False
    # 3*3方格內不能有重複的
    m,n = 0,0
    for g in range(3):
        for k in range(3):
            temp = [] # 儲存相同數據用
            for i in range(3):
                for j in range(3):
                    if board[i+m][j+n] != ".":
                        temp.append(board[i+m][j+n])
            if len(list(set(temp))) != len(temp):
                return False
            n+=3
        n=0
        m+=3
    return True




print(isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))


