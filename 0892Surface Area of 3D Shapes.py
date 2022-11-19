def surfaceArea(grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == n == 1:
            return 6 + 4*(grid[0][0]-1)
        bt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    bt += 1
        bt = bt*2
        ans = 0
        for i in range(m):
            for j in range(n-1):
                if j==0:
                    ans += abs(grid[i][j]-grid[i][j+1])
                else:
                    if i==0 or i==m-1:
                        ans += abs(grid[i][j]-grid[i][j+1]) + grid[i][j]
                    else:
                        ans += abs(grid[i][j]-grid[i][j+1])
        for i in range(n):
            for j in range(m-1):
                if j==0:
                    ans += abs(grid[j][i]-grid[j+1][i])
                else:
                    if i == 0 or i==n-1:
                        ans += abs(grid[j][i]-grid[j+1][i]) + grid[j][i]
                    else:
                        ans += abs(grid[j][i]-grid[j+1][i])
        ans += 2*(grid[0][0]+ grid[0][n-1] + grid[m-1][0] + grid[m-1][n-1])
        return ans + bt





def surfaceArea2(grid: list[list[int]]) -> int:
        xy, xz, yz, count = 0, 0, 0, 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    count+=1
            xz+=max(grid[i])
        xy = count
        for j in range(m):
            countrow = 0
            for i in range(n):
                countrow = max(countrow, grid[i][j])
            yz+=countrow
        if n < 2 and m < 2:
            return (xy+xz+yz)*2
        low = 0        
        for i in range(1, n-1):
            for j in range(1, m-1):
                test = [grid[i-1][j], grid[i][j-1], grid[i][j+1], grid[i+1][j]]
                if grid[i][j] <= min(test):
                    low += sum(test) - grid[i][j]*4   
        print(low)
        for j in range(1, m-1):
            if grid[0][j] < grid[0][j-1] and grid[0][j] < grid[0][j+1]:
                low += (min(grid[0][j-1], grid[0][j+1]) - grid[0][j])*2
            if grid[-1][j] < grid[-1][j-1] and grid[-1][j] < grid[-1][j+1]:
                low += (min(grid[-1][j-1], grid[-1][j+1]) - grid[-1][j])*2
        print(low)
        for i in range(1, n-1):
            if grid[i][0] < grid[i-1][0] and grid[i][0] < grid[i+1][0]:
                low += min(grid[i-1][0], grid[i+1][0]) - grid[i][0]*2
            if grid[i][-1] < grid[i-1][-1] and grid[i][-1] < grid[i+1][-1]:
                low += (min(grid[i-1][-1], grid[i+1][-1]) - grid[i][-1])*2
        print(low)
        return (xy+xz+yz)*2 + low
    
    
print(surfaceArea([[4,0,2],[1,2,3],[2,3,5]]))