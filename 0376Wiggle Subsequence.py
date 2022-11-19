def wiggleMaxLength(nums: list[int]) -> int:
        ans = []
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]:
                ans.append(nums[i+1] > nums[i])
        i, n = 0, len(ans)
        while i < n-1:
            print(i,n, ans)
            if ans[i] == True and ans[i+1] == True:
                del ans[i]
                n-=1
            elif ans[i] == False and ans[i+1] == False:
                del ans[i]
                n-=1
            else:
                i+=1
        return len(ans) + 1
        
        
        
        
        
        
print(wiggleMaxLength([1,7,4,9,2,5]))
print(wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
print(wiggleMaxLength([0,0]))