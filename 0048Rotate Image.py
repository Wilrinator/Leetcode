def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for r in range(len(matrix)):
        for c in range(r, len(matrix)):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in range(len(matrix)):
        matrix[r] = matrix[r][::-1]
    print(matrix)

def rotate2(matrix: list[list[int]]):
    n = len(matrix)
    for i in range(n):
        matrix.append([])
    i,j = 0,0
    while i < n+1 and j < n+1:
        if i == n:
            break
        matrix[j+n].insert(0, matrix[i][j])
        j += 1
        if j == n:
            j = 0
            i += 1
    matrix = matrix[n:]
    return matrix





print(rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))