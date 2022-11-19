def canJump2(nums: list[int]) -> bool:
    for idx in range(len(nums)-1):
        print(idx, nums)
        if nums[idx] == 0:
            return False
        nums[idx+1] = max(nums[idx]-1,nums[idx+1])
    return True

def canJump(nums: list[int]) -> bool:
    n, ans, i= len(nums), [1], 0
    if len(nums) < 2:
        return True
    while i < n:
        if len(ans) > n:
            return True
        for j in range(nums[i]):
            print(j, i, nums[i], ans)
            if len(ans) <= i:
                return False
            elif len(ans) <= nums[i] + i:
                ans.append(ans[i] + 1)
                j += 1
            else:
                break
        i += 1
    print(ans)
    if len(ans) < len(nums):
        return False
    return True





print(canJump2([2,3,1,1,4]))