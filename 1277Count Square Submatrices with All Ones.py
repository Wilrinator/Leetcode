def countSquares2(matrix):
    m, n, Ans = len(matrix[0]), len(matrix), 0
    if n == 1:
        return sum(matrix[0])
    elif m == 1:
        for i in range(n):
            Ans += matrix[i][0]
        return Ans
    else:
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
    for i in range(n):
        Ans += sum(matrix[i])
    return Ans




def countSquares3(matrix):
    count = sum(matrix[0])

    for i in range(1, len(matrix)):
        count += matrix[i][0]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                continue
            matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
            print(matrix)
            count += matrix[i][j]

    return count



def countSquares(matrix: list[list[int]], Mat = [], Ans = 0) -> int:
    print("Ans =", Ans)
    if Ans == 0:
        Mat = matrix
    count, m, n, temp = 0, len(Mat[0]), len(Mat), []
    print("Mat =", Mat)
    if n == 1:
        print("final line")
        count = sum(Mat[0])
        return Ans + count
    elif m == 1:
        print("one Row")
        for i in range(n):
            count += Mat[i][0]
        return Ans + count
    else:
        for i in range(n):
            count += sum(Mat[i])
        print("count = ", count)
    for k in range(n-1):
        temp.append([])
        for l in range(m-1):
            if Mat[k][l] == 1 == Mat[k+1][l] == Mat[k+1][l+1] == Mat[k][l+1]:
                temp[k].append(1)
            else:
                temp[k].append(0)

    Ans += count
    return countSquares(matrix, temp, Ans)



print(countSquares2([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))


