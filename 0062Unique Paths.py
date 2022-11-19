def uniquePaths(m: int, n: int):
    Ans, i, j, ans= [[1]], 1, 1, []
    for i in range(m-1):
        Ans[0].append(1)
    for j in range(n):
        ans.append(Ans[0])
    print(ans)
    for i in range(1,n):
        for j in range(1,m):
            ans[i][j] = ans[i-1][j] + ans[i][j-1]
            print(i,j, ans)
    return ans[-1][-1]

print(uniquePaths(3,7))
