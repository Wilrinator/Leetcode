def largestTriangleArea(points: list[list[int]]) -> float:
        Area = 0        
        for i in range(0, len(points)-2):            
            for j in range(i+1, len(points)-1):
                for k in range(j+1, len(points)):
                    A1 = (points[i][1] + points[j][1])*abs(points[i][0] - points[j][0]) 
                    A2 = (points[k][1] + points[j][1])*abs(points[k][0] - points[j][0])  
                    A3 = (points[k][1] + points[i][1])*abs(points[k][0] - points[i][0]) 
                    A = abs(A1+A2-A3)
                    print(A1,A2,A3, A, i , j ,k)
                    Area = max(Area, A/2)              
        return Area
    
print(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))