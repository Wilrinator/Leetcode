def pivotIndex(self, nums: List[int]) -> int:
    s, Sum = sum(nums), 0
    for i in range(len(nums)):
        if Sum == (s - nums[i]) / 2:
            return i
        Sum += nums[i]
    return -1