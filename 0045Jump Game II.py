def jump(self, nums: list[int]) -> int:
    n, ans, i = len(nums), [0], 0
    if len(nums) < 2:
        return 0
    while i < n:
        for j in range(nums[i]):
            if len(ans) <= i:
                break
            elif len(ans) <= nums[i] + i:
                ans.append(ans[i] + 1)
                j += 1
            else:
                break
        i += 1
    return ans[n - 1]