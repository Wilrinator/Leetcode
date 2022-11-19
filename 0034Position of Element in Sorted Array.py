def searchRange(nums: list[int], target: int) -> list[int]:
    ans = [-1,-1]
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)
            ans[0] = i
            break
    print(ans)
    if ans[0] == -1: return ans
    if len(nums) == 1: return [0, 0]
    for i in range(len(nums)):
        if nums[-i-1] == target:
            ans[1] = len(nums) - i -1
            return ans




#print(searchRange(nums = [5,7,7,8,8,10], target = 8))
#print(searchRange(nums = [5,7,7,8,8,10], target = 6))
print(searchRange(nums = [1,3], target = 1))