def exist(board, word: str) -> bool:
        n = len(board[0])
        m = len(board)
        start = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append([i,j])
        print("start =", start)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        jmax=0
        for i in start:
            j = 1
            while j < len(word):
                print("start =", start, j)
                for di, dj in directions:
                    print(di,dj,i)
                    ii, jj = i[0] + di, i[1] + dj
                    if 0 <= ii < m and 0 <= jj < n and j < len(word):
                        print(ii,jj,j)
                        if board[ii][jj] == word[j]:
                            i[0] = ii
                            i[1] = jj
                            j+=1
                start.pop(0)   
            jmax=max(jmax,j)                  
                        
                            
        if j == len(word):
            return True
        else:
            return False
        
        
def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])        
        def get_neighbors(i,j):
            return [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]        
        def is_valid(i,j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False        
        def dfs(i, j, index):
            if index == len(word):
                return True
            for nei in get_neighbors(i,j):
                x, y = nei
                if is_valid(x, y) and (x,y) not in visited and board[x][y] == word[index]:
                    visited.add((x,y))
                    if dfs(x, y, index+1):
                        return True
                    visited.remove((x,y))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    if dfs(i,j,1):
                        return True
        return False        
        

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))