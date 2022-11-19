def maxPoints(points: list[list[int]]) -> int:
    m, n = len(points[0]), len(points)
    Source = points[0]
    if n == 1:
        return max(points[0])
    for i in range(1, n):
        for j in range(m):
            temp, k = 0, 0
            while k < m:
                if Source[k] - abs(j - k) > temp:
                    temp = Source[k] - abs(j - k)
                k += 1
            points[i][j] += temp
        Source = points[i]
    return max(points[-1])

def maxPoints2(points: list[list[int]]) -> int:
    Ans, m, n = points[0], len(points[0]), len(points)
    if n == 1:
        return max(Ans)
    for i in range(1, n):
        temp = 0
        for j in range(m):
            temp = max(temp-1, Ans[j])
            Ans[j] = temp
        temp = 0
        for j in range(m-1, -1, -1):
            temp = max(temp-1, Ans[j])
            Ans[j] = temp
        for j in range(m):
            points[i][j] += Ans[j]
        Ans = points[i]
    return max(points[-1])



print(maxPoints([[5,2,1,2],[2,1,5,2],[5,5,5,0]]))
print(maxPoints2([[5,2,1,2],[2,1,5,2],[5,5,5,0]]))

