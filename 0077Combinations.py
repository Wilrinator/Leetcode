def combine(n: int, k: int):
    base = []        
    def permu(step, base):                
            if step == 0:
                return base
            else:
                check = []
                for i in base:   
                    temp = i[:]
                    for j in range(i[-1]+1, n+1):                        
                        temp.append(j)
                        check.append(temp)   
                        if j < n:
                            temp = i[:]
                return permu(step-1, check)            
    for i in range(1, n-k+2):
        base.append([i])
    return permu(k-1, base)


def combine2(n: int, k: int) :
        ans = []
        def helper(combination, start, remaining_slots):
            if remaining_slots == 0:
                ans.append(combination)
            else:
                for num in range(start, n + 1):
                    helper(combination + [num], num + 1, remaining_slots - 1)
                    print(combination)
        helper([], 1, k)
        return ans
        
        
print(combine(5, 3))



def combine3(self, n, k):
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k, path+[nums[i]], ret)