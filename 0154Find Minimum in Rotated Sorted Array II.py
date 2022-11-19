def findMin(nums: list[int]) -> int:
        low, mid, high = 0,0, len(nums)-1
        while low<high:
            mid = low+(high-low)//2
            if nums[mid]>nums[high]: low = mid+1
            elif nums[mid]< nums[high]: high = mid
            else: high -=1
        return nums[low]



def findMin2(nums: list[int]) -> int:
        start = len(nums)
        for i in range(start):
            if i < start-1 and nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]