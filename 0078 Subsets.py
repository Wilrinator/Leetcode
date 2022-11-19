import copy

def subsets(nums):
        ans = [[]]
        for i in range(len(nums)):
            temp = copy.deepcopy(ans)
            for j in range(len(temp)):     
                   
                temp[j].append(nums[i])
                print(j , "temp =", temp[j], "ans =", ans) 
                ans.append(temp[j])
        return ans
    
    
print(subsets([1,2,3]))


def subsets2(self, nums):
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
    
    
    
def subsets3(self, nums):
        def backtrack(first = 0, curr = []):
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output