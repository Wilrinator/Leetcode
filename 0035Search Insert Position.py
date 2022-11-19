def searchInsert(self, nums: list[int], target: int) -> int:
    ans = -1
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    if ans == -1:
        for i in range(len(nums)):
            if nums[i] > target:
                return i

