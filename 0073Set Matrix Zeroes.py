def setZeroes(matrix: list[list[int]]) -> None:
        row, column = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        print(row, column)
        for k in row:            
            for l in range(len(matrix[0])):                
                matrix[k][l] = 0           
        for m in range(len(column)):
            for n in range(len(matrix)):
                matrix[n][m] = 0
        print(matrix)
                
print(setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))