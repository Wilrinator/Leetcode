def nextPermutation(nums: list[int]) -> list[int]:
    a = len(nums)
    temp = list(nums)
    if a == 1: return nums
    for i in range(1,a):
        if nums[-i-1] < nums[-i]:
            print("swap")
            k = -i-1
            print(nums[k], nums[-i], nums[k+1:])
            mi = 101
            check = nums[k+1:]
            for j in check:
                if mi > j and j > nums[k]:
                    mi = j
            ex = nums[::-1].index(mi)
            print(ex, nums[k], nums[-ex-1])
            nums[k], nums[-ex-1] = nums[-ex-1], nums[k]
            print(nums)
            nums[k+1:] = nums[k+1:][::-1]
            break
    if temp == nums:
        nums.sort()
    return nums








# print(nextPermutation(nums = [1,3,2]))
print(nextPermutation(nums = [5,4,7,5,3,2]))
#print(nextPermutation(nums = [1,1,3]))
#print(nextPermutation(nums = [1,4,2,3]))