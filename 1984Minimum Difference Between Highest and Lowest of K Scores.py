def minimumDifference(nums: list[int], k: int) -> int:
    n, ans = len(nums) - k, 10000
    nums.sort()
    if n == 0:
        return 0
    for i in range(n+1):
        print(i, i + k - 1, ans)
        if ans > nums[i + k - 1] - nums[i]:
            ans = nums[i + k - 1] - nums[i]
    return ans


print(minimumDifference(nums = [9,4,1,7], k = 2))