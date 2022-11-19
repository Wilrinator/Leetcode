def sortColors(nums: list[int]):
    if len(nums) == 1:
        return nums
    i, count = 0, 0
    while count < len(nums):
        if nums[i] == 2:
            nums.pop(i)
            nums.append(2)
            count += 1
        elif nums[i] == 0:
            nums.pop(i)
            nums.insert(0, 0)
            i += 1
            count += 1
        else:
            i += 1
            count += 1
    return nums

print(sortColors([0,0]))