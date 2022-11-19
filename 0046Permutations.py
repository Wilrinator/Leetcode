def permute(nums: list[int]) -> list[list[int]]:
    ans, curr, n = [], [], len(nums)
    def dfs(curr, nums, idx):
        if len(curr) == n:
            ans.append(curr[:])
            return
        for i in range(idx, n):
            curr.append(nums[i])
            print(curr, idx, i)
            dfs(curr, nums, i+1)
            curr.pop()
    dfs([], nums, 0)
    return ans


def permute2(nums):
    def permut(nums, step, ans):
        if step == 0:
            return permut(nums, 1, [[nums[0]]])
        elif step == len(nums):
            return ans
        else:
            check = []
            for i in range(len(ans)):
                for j in range(len(ans[0])+1):
                    temp = ans[i][:]
                    print(i,j,step,temp,check)
                    temp.insert(j, nums[step])
                    check.append(temp)
            return permut(nums, step+1, list(check))
    return permut(nums, 0, [])




                    
def permute3(self, nums):
    res = []
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    self.dfs(nums, [], res)
    return res
    

print(permute2(nums = [1,2,3]))

