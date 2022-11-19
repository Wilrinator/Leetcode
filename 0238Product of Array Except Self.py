def productExceptSelf(self, nums: List[int]) -> List[int]:
    res, acc = [], 1
    for n in nums:
        res.append(acc)
        acc *= n
    acc = 1
    for i in reversed(range(len(nums))):
        res[i] *= acc
        acc *= nums[i]
    return res


def productExceptSelf2(nums: list[int]) -> list[int]:
    result, ans, make = 1, [], []
    for i in range(len(nums)):
        if nums[i] == 0:
            make.append(i)
            continue
        result = result * nums[i]
    if len(make) == 1:
        for i in range(len(nums)):
            if i == make:
                ans.append(result)
                continue
            ans.append(0)
        return ans
    elif len(make) > 1:
        for i in range(len(nums)):
            ans.append(0)
        return ans
    for i in nums:
        ans.append(int(result / i))
    return ans



print(productExceptSelf([1,2,3,4]))