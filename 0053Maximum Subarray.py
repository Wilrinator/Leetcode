def maxSubArray(nums: list[int]) -> int:
    ans, i = 0, 0
    while i < len(nums):
        temp = 0
        if nums[i] > 0:
            while i < len(nums):
                temp += nums[i]
                if temp < 0:
                    break
                elif temp > ans:
                    ans = temp
                i += 1
        else:
            i += 1
    if ans == 0:
        return max(nums)
    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
#print(maxSubArray([1]))
#print(maxSubArray([5,4,-1,7,8]))