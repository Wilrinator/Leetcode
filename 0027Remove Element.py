def removeElement2(nums: list[int], val: int) -> int:
    i = 0
    while val in nums:
        print(i, nums)
        if nums[i] == val:
            nums.pop(i)
            i-=1
        i+=1
    print(nums)
    return len(nums)

def removeElement(nums: list[int], val: int) -> int:
    nums = list(filter(lambda a: a != val, nums))
    print(nums)
    return len(nums)








print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))
#print(removeElement(nums = [3,2,2,3], val = 3))