def largestSumAfterKNegations(nums: list[int], k: int) -> int:
    nums.sort()
    i = 0
    n = len(nums)
    while (i < n and k > 0):
        if nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        elif nums[i] >= 0:
            break
    if k % 2 == 1:
        return sum(nums) - 2 * (min(nums))
    else:
        return sum(nums)



def largestSumAfterKNegations2(nums: list[int], k: int) -> int:
    pos, zero, neg = [], [], []
    for i in nums:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i * -1)
        else:
            zero.append(i)
    if len(neg) == 0:
        if k % 2 != 0:
            pos.sort()
            pos[0] *= -1
        elif len(zero) != 0:
            return sum(pos)
        return sum(pos)
    else:
        neg.sort()
        if k < len(neg):
            for i in range(len(neg) - k):
                neg[i] *= -1
        else:
            if (k - len(neg)) % 2 != 0 and len(zero) == 0:
                pos.sort()
                if len(pos) == 0 or pos[0] > neg[0]:
                    neg[0] *= -1
                else:
                    pos[0] *= -1
        return sum(pos) + sum(neg)


print(largestSumAfterKNegations([-4,-2,-3], 4))