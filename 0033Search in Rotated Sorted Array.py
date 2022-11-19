def search2(nums: list[int], target: int) -> int:
    ans = -1
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    if ans == -1:
        return ans
    
def search(nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid            
            if nums[l]<=nums[mid]:
                if target > nums[mid] or target<nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1            
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1                
        return -1


print(search(nums = [4,5,6,7,0,1,2], target = 0))
print(search(nums = [4,5,6,7,0,1,2], target = 3))
print(search(nums = [1], target = 0))