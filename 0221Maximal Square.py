def maximalSquare(matrix: list[list[str]]) -> int:
    m, n, Ans, temp = len(matrix[0]), len(matrix), 0, []
    for i in range(n):
        integer_map = map(int, matrix[i])
        temp.append([])
        temp[i] += list(integer_map)
        if max(temp[i]) > Ans:
            Ans = max(temp[i])
    if n == 1 or m == 1:
        return Ans
    for i in range(1, n):
        for j in range(1, m):
            if temp[i][j] == 0:
                continue
            temp[i][j] = min(temp[i - 1][j], temp[i][j - 1], temp[i - 1][j - 1]) + 1
            if temp[i][j] > Ans:
                Ans = temp[i][j]
    return Ans ** 2



print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalSquare([["1","0"],["0","0"]]))