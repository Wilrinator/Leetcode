def minPathSum(grid: list[list[int]]) -> int:
    m, n = len(grid[0]), len(grid)
    ans = grid[:]
    for j in range(1, n):
        ans[0][j] += ans[0][j-1]
    for i in range(1, m):
        ans[i][0] += ans[i-1][0]
    for i in range(1, n):
        for j in range(1, m):
            ans[i][j] += min(ans[i-1][j], ans[i][j-1])
    return ans[-1][-1]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))