def maxProduct(nums: list[int]) -> int:
    currMax, currMin = 1, 1
    res = nums[0]
    for n in nums:
        vals = (n, currMax * n, currMin * n)  # tuples can enhance time-complexity
        currMax, currMin = max(vals), min(vals)
        res = max(res, currMax)
        print(res)
    return res



def maxProduct2(nums: list[int]) -> int:
    ans, n = [], len(nums)
    if n == 1:
        return nums[0]
    for i in range(n):
        if nums[i] == 1:
            ans = max(ans, 1)
            continue
        product = 1
        for j in range(i, n):
            if nums[j] == 1:
                continue
            product *= nums[j]
            ans = max(ans, product)
    return max(ans)



print(maxProduct(nums = [2,3,-2,4]))