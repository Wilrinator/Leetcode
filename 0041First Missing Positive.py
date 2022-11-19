def firstMissingPositive3(nums: list[int]) -> int:
    for i in range(1, len(nums)+1):
        if i not in nums:
            return i
    return len(nums) + 1

def firstMissingPositive(nums: list[int], i=1) -> int:
    seen = {}
    for i, x in enumerate(nums):
        if x not in seen:
            seen[x] = i
    for x in range(1, len(nums) + 1):
        if x not in seen:
            return x
    return len(nums) + 1


def firstMissingPositive2(nums: list[int], i=1) -> int:
    if i not in nums:
        return i
    else:
        return firstMissingPositive(nums, i + 1)


print(firstMissingPositive(nums = [1,2,0]))
print(firstMissingPositive(nums = [3,4,-1,1]))
print(firstMissingPositive(nums = [7,8,9,11,12]))