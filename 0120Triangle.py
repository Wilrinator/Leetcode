def minimumTotal(triangle: list[list[int]], i = 1, ans = [0], count = 1) -> int:
    n, m = len(triangle), len(ans)
    if i == 1:
        ans = triangle[0]
    else:
        for j in range(m):
            ans.append(ans[j] + triangle[i - 1][j])
            ans.append(ans[j] + triangle[i - 1][j+1])
        for j in range(m):
            ans.pop(0)
    if i >= 3:
        for j in range(count):
            ans[j+1] = min(ans[j+1],ans[j+2])
            ans.pop(j+2)
        count += 1
    i += 1
    if i > n:
        return min(ans)
    else:
        return minimumTotal(triangle, i, ans, count)






print(minimumTotal([[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]))