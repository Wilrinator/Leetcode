def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m, n, obs = len(obstacleGrid[0]), len(obstacleGrid), []
    for i in range(n):
        for j in range(m):
            if obstacleGrid[i][j] == 1:
                obs.append(i)
                obs.append(j)
    Ans, i, ans= [[1]], 1, []
    while i < m:
        Ans[0].append(0)
        i+=1
    i = 1
    while i < n+1:
        ans += Ans[:]
        i+=1
    for i in range(n):
        if len(obs) > 0:
            if i == obs[0]:
                if obs[1] == 0:
                    ans[i][0] *= 0
                    obs = obs[2:]
        for j in range(1, m):
            ans[i][j] = ans[i-1][j] + ans[i][j-1]
            print(i, j , ans)
            if len(obs) > 0:
                if i == obs[0]:
                    if j == obs[1]:
                        ans[i][j] *= 0
                        obs = obs[2:]
    return ans[-1][-1]


print(uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))