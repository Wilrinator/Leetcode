def findDuplicate(nums: list[int]) -> int:
        ans = {}
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans[nums[i]] = i
            else:
                return nums[i]
            
            
print(findDuplicate([3,1,3,4,2]))