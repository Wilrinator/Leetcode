def numIslands(grid):
        X = len(grid)
        Y = len(grid[0]) 
        def cleanse(a,b):
            print(a,b)
            grid[a][b] = "0"
            if a+1 < X and grid[a+1][b] == "1":
                cleanse(a+1,b)
            if b+1 < Y and grid[a][b+1] == "1":
                cleanse(a,b+1)
            return        
        count = 0
        for x in range(X):
            for y in range(Y):
                if grid[x][y] == "1":
                    count+=1
                    cleanse(x,y)
        return count
    
    
print(numIslands(grid = 
[["1","1","1"],["0","1","0"],["1","1","1"]]))