def majorityElement(self, nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


def majorityElement2(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums) // 2
    return nums[n]