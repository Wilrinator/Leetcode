def orangesRotting(grid):
        m = len(grid)
        n = len(grid[0])
        mark = []
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    mark.append([i,j])
                elif grid[i][j] == 1:
                    ones += 1
        def spread(grid, mark, step, ones):
            Mark = []
            a,b, change = 0, 0, 0
            for i in mark:
                [a, b] = i
                for A,B in [[a-1,b],[a+1,b],[a,b+1],[a,b-1]]:
                    if A<0 or B<0 or A>=m or B>=n or grid[A][B]!=1:
                        continue
                    grid[A][B] = 2
                    change += 1
                    ones-=1
                    Mark.append([A,B])
            if change == 0:
                if ones >0: step = -1
                return step
            else: 
                return spread(grid, Mark, step+1, ones)           
        step = 0
        return spread(grid, mark, step, ones)
                
print(orangesRotting([[2,2,2,1,1]]))