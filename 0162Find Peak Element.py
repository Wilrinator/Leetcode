def findPeakElement(arr: list[int]) -> int:
        low, high = 0, len(arr)-1
        
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[mid+1]:
                high = mid
            else:
                low = mid + 1				
        return low


def findPeakElement2(nums: list[int]) -> int:
        start = len(nums)
        for i in range(start):
            if i < start-1 and nums[i] > nums[i+1]:
                return i
        return start-1
    
print(findPeakElement([1,2,3,1]))