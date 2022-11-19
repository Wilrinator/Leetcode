def search(nums: list[int], target: int) -> bool:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start) // 2  
            if nums[mid] == target:
                return True
            if nums[mid] == nums[start] ==  nums[end]:
                for i in nums:
                    if target==i:
                        return True
                return False
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1           
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1           
        return False




def search(nums: list[int], target: int) -> bool:
        start = len(nums)
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] > nums[i+1]:
                start = i
                break
        if target < nums[0]:
            for i in nums[start:]:
                if target == i:
                    return True
            return False
        for i in nums[0 : start+1]:
            if target == i:
                return True
        return False