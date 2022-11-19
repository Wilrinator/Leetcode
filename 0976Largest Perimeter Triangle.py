def largestPerimeter(self, nums: List[int]) -> int:
    nums.sort()
    for i in range(len(nums) - 2):
        if nums[-i - 1] < nums[-i - 2] + nums[-i - 3]:
            return nums[-i - 1] + nums[-i - 2] + nums[-i - 3]
    return 0