def rob(nums: list[int]) -> int:
    n, ans = len(nums), nums
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    if n == 3:
        return max(nums[0] + nums[2], nums[1])
    else:
        ans[2] += ans[0]
        for i in range(3, n):
            ans[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])


def rob2(nums: list[int]) -> int:
    o1 = o2 = o3 = 0

    for n in nums:
        o1, o2, o3 = max(o2, o3) + n, o1, o2
        print(o1, o2, o3)

    return max(o1, o2, o3)



print(rob2([6,3,10,8,2,10,3,5,10,5,3]))