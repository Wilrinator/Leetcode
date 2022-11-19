def spiralOrder2(matrix: list[list[int]], ans=[]) -> list[int]:
    if count == 0:
        ans = []
    for i in range(len(matrix[0])):
        ans.append(matrix[0][i])
    del matrix[0]
    if matrix == []: return ans
    for j in range(len(matrix)):
        ans.append(matrix[j][-1])
        del matrix[j][-1]
    for k in range(len(matrix[-1])):
        ans.append(matrix[-1][-k - 1])
    del matrix[-1]
    if matrix == [] or matrix[0] == []: return ans
    for l in range(len(matrix)):
        ans.append(matrix[-1 - l][0])
        del matrix[-l - 1][0]
    else:
        return self.spiralOrder(matrix, ans, count + 1)



def spiralOrder(matrix) -> list[int]:
        
        def visit_up(r, c):
            if r < 0 or [r,c] in vis:
                return
            
            res.append(matrix[r][c])
            vis.append([r,c])
            visit_up(r-1, c)
            visit(r, c+1)
            visit(r+1, c)
            visit(r, c-1)
            
        
        def visit(r,c):
            
            if r < 0 or c < 0 or r > m-1 or c > n-1 or [r,c] in vis:
                return
            
            res.append(matrix[r][c])
            vis.append([r,c])
            
            visit(r, c+1)
            visit(r+1, c)
            visit(r, c-1)
            visit_up(r-1, c)
        
        m, n = len(matrix), len(matrix[0])
        res = []
        vis = []
        visit(0, 0)
        return res


print(spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))