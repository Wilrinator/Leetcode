def maxArea(height) -> int:
    if len(height) == 0:
        return 0
    Area = 0
    b = 0
    h = 0
    for i in range(len(height)):
        for j in range(i,len(height)):
            h = min(height[i],height[j])
            b = j-i
            if Area < b*h:
                Area = b*h
    return Area


def maxArea2(height: list[int]) -> int:
        Area = 0
        l = len(height)
        i = 0
        j = l-1
        while i < j:
            Area = max(Area, (j-i)*min(height[i],height[j]))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1                
        return Area



print(maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(maxArea(height = [1,1]))
print(maxArea(height = [4,3,2,1,4]))
print(maxArea(height = [1,2,1]))