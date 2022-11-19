def cyclicSort(nums):
        i = 0
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] == nums[correct]:
                i += 1
            else:
                nums[i], nums[correct] = nums[correct], nums[i]
                
def findErrorNums(nums: list[int]) -> list[int]:
    cyclicSort(nums)
    print(nums)
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i+1]





def findErrorNums2(nums: list[int]) -> list[int]:
    res = 0
    for i in range(1, len(nums)+1):
        res ^= (i ^ nums[i-1])
# Will give you the position of the rightmost set bit
    res = (res & -res)
    res1 = 0
    res2 = 0
    for i in range(len(nums)):
        if nums[i] & res > 0:
            res1 ^= nums[i]
        else:
            res2 ^= nums[i]
    for i in range(1, len(nums)+1):
        if i & res > 0:
            res1 ^= i
        else:
            res2 ^= i
    for i in range(len(nums)):
        if nums[i] == res1:
            return [res1, res2]
    return [res2, res1]




def findErrorNums3(nums: list[int]) -> list[int]:
        res = sum(set(nums))
        return [sum(nums) - res ,sum(range(1,len(nums)+1))  - res]



def findErrorNums4(nums: list[int]) -> list[int]:
        check = list(range(1,len(nums)+1))
        ans = {}
        a, b = 0, 0
        for i in range(len(nums)):
            if b == 0:
                if check[i] not in nums:
                    b = check[i]
                    if a != 0:
                        break
            if a == 0:
                if nums[i] not in ans:
                    ans[nums[i]] = i
                else:
                    a = nums[i]
                    if b != 0:
                        break
        return [a, b]
    
    
print(findErrorNums([1,5,3,2,2,7,6,4,8,9]))