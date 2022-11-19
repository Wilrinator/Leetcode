def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        count = m-1
        for i in range(m):
            if matrix[i][0] <= target:
                count = i
            else: break
        for j in range(n):
            if matrix[count][j] > target:
                return False
            elif matrix[count][j] == target:
                return True
        return False   



def searchMatrix2(matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while i < m and j < n:
            if target > matrix[i][j]:
                if i+1 <m and matrix[i+1][j] <= target:
                    i+=1
                else:
                    j+=1            
            else:
                return matrix[i][j] == target
        return False