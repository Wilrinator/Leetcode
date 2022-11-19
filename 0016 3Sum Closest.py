def threeSumClosest(nums, target) -> int:
    nums.sort()
    Ans = 0
    Abs = 2000
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                Sum = nums[i] + nums[j] + nums[k]
                if Abs > abs(Sum - target):
                    Abs = abs(Sum - target)
                    Ans = Sum
                if Ans == target:
                    return Ans
    return Ans


def threeSumClosest2(nums, target) -> int:
    nums.sort()
    Ans = 0
    Abs = 2000
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        while j < k:
            print(i,j,k)
            Sum = nums[i] + nums[j] + nums[k]
            if Abs > abs(Sum - target):
                Abs = abs(Sum - target)
                Ans = Sum
                if Ans == target: return Ans
            if Sum <= target:
                j += 1
            else:
                k -= 1
    return Ans


#print(threeSumClosest(nums = [-1,2,1,-4], target = 1))
#print(threeSumClosest(nums = [0,0,0], target = 1))
#print(threeSumClosest([1,1,1,0],-100))
#print(threeSumClosest([1,2,5,10,11],12))
print(threeSumClosest2([1,2,4,8,16,32,64,128],82))