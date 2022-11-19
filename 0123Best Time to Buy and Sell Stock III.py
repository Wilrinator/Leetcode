def maxProfit(prices):
        ans, Min, Max = [],10000,0
        for n in range(len(prices)-1):            
            Min = min(prices[n], Min)
            Max = prices[n]
            ans.append(prices[n+1] - prices[n])
        print(ans)
        for i in range(len(ans)-1):
            if ans[i] > 0:
                if ans[i+1] >= 0:
                    ans[i+1] += ans[i]
                    ans[i] = 0
            elif ans[i] < 0:
                ans[i] = 0
        print(ans)
        ans.sort()            
        return ans[-1] + ans[-2]
    
print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([1,2,4,2,5,7,2,4,9,0]))