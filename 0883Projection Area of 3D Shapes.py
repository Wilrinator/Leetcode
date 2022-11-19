def projectionArea(grid: list[list[int]]) -> int:
        xy, xz, yz, count = 0, 0, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    count+=1
            xz+=max(grid[i])
        xy = count
        for j in range(len(grid[0])):
            countrow = 0
            for i in range(len(grid)):
                countrow = max(countrow, grid[i][j])
            yz+=countrow
        print(xy,xz,yz)
        return xy+xz+yz
    
print(projectionArea([[1,2],[3,4]]))
print(projectionArea([[1,0],[0,2]]))