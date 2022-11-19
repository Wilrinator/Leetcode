def rob(nums: list[int]) -> int:
    n, ans, Ans = len(nums), nums[1:], list(nums[:-1])
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    if n == 3:
        return max(nums[0], nums[2], nums[1])
    else:
        ans[2] += ans[0]
        Ans[2] += Ans[0]
        for i in range(3, n-1):
            ans[i] += max(ans[i-2], ans[i-3])
            Ans[i] += max(Ans[i - 2], Ans[i - 3])
        return max(ans[-1], ans[-2], Ans[-1], Ans[-2])
