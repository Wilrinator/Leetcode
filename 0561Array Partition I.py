def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    ans, i = 0, 0
    while i < len(nums):
        ans += min(nums[i], nums[i + 1])
        i += 2
    return ans