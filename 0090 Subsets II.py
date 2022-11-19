import copy

def subsetsWithDup2(nums):
        nums.sort()
        ans = [[]]
        for i in range(len(nums)):
            temp = copy.deepcopy(ans)
            for j in range(len(temp)):
                temp[j].append(nums[i])
                if temp[j] not in ans:
                    ans.append(temp[j])
        return ans
    
    
    
def subsetsWithDup(nums):
        nums.sort()
        res=[]
        helper(res,nums,[])
        return res 
def helper(res,nums,path):
        res.append(path)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            print("path", path)
            helper(res,nums[i+1:],path+[nums[i]])    
    
    
print(subsetsWithDup([4,2,4,1,4,3]))