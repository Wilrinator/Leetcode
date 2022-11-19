def removeDuplicates(nums):  #用sorted來排列、用sorted來清除重複項目
    ans = set(nums)
    for i in range(len(ans)):
        nums[i] = sorted(list(ans))[i]
    print(nums)
    return len(ans)






print(removeDuplicates([-1,0,0,0,0,3,3]))