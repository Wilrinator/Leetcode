def find132pattern2(nums: list[int]) -> bool:
        stack = []
        s2 = float('-inf')
        for i in nums[::-1]:
            print(stack, i, s2)
            if i<s2: return True
            while stack and i>stack[-1]: 
                s2 = stack.pop()
            stack.append(i)
        return False



def find132pattern(nums: list[int]) -> bool:
        mi = [nums[0]]        
        n = len(nums)        
        for j in range(1,n):
            mi.append(min(mi[-1],nums[j]))           
        print(mi)      
        stack=[]                
        for j in range(n-1,-1,-1):    
            print(stack, mi[j], nums[j])
            while stack and stack[-1] <= mi[j]:
                stack.pop()
            if len(stack) > 0:
                if mi[j] < stack[-1] < nums[j]:
                    return True
            stack.append(nums[j])        
        return False
    
    
print(find132pattern2([3,2,0,3,5,0,1,3,2,1,0,-2,-3,4]))