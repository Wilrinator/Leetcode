def canPartition(nums) -> bool:        
        Sum = 0
        for i in nums:
            Sum += i
        if Sum%2 == 1:
            return False
        else:
            target = Sum/2
            print("target is", target)
            if target in nums:
                return True
            Sol = set()
            m = len(nums)            
            for i in range(m):
                temp = nums[i]
                for j in range(i+1, m):
                    for k in range(j+1, m):
                        temp+=nums[k]
                        Sol.add(temp)
                        temp-=nums[k]
                    temp+=nums[j]
                    Sol.add(temp)
            print(Sol)
            if target in Sol:
                return True
            else:
                return False
            
            
def canPartition2(nums) -> bool:        
        Sum = sum(nums)        
        if Sum%2 == 1:
            return False
        target = Sum/2
        n = len(nums)            
        cache = {}
        
        def dfs(nums, target):
            print(nums, target, cache)
            if target == 0:
                return True
            if target in cache:
                return cache[target]
            for i in range(len(nums)):
                if nums[i] <= target and dfs(nums[:i] + nums[i +1:], target - nums[i]):
                    return True
            cache[target] = False
            return False
        return dfs(nums,target)
    
    
    
def canPartition3(nums) -> bool:
        if len(nums) < 2:
            return False
        value_sum = sum(nums)
        if value_sum % 2 == 1:
            return False
        m = len(nums)
        n = value_sum // 2

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(m):
            for j in range(n, 0, -1):
                print(i,j,dp)
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[n]

print(canPartition3([23,13,11,7,6,5,5]))