def findMin(nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while(left <= right):
            mid = (left + right) // 2
            if (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                break
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            
        return nums[(mid+1)%len(nums)]


def findMin(nums: list[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] > nums[i+1]:
                return nums[i+1]