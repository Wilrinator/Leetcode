def missingNumber(nums: list[int]) -> int:
    return list(set(list(range(0,len(nums)+1)))-set(nums))[0]
    
    
    
def missingNumber2(nums: list[int]) -> int:  
    return int((len(nums)*(len(nums)+1))/2-sum(nums))






def missingNumber3(nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != nums[i]:
                return i
        return n