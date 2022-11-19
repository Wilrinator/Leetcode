def findMiddleIndex(self, nums: list[int]) -> int:
    s, Sum = sum(nums), 0
    for i in range(len(nums)):
        if Sum == (s - nums[i]) / 2:
            return i
        Sum += nums[i]
    return -1