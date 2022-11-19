def coinChange2(coins, amount: int) -> int:
        coins.sort()
        Ans=[0]
        def reCur(coins, amount, Ans, Next, M):
            Curr = len(Ans)
            temp = []
            if amount == Curr-1:
                if M == 1 and Ans[-1] == 0:
                    Ans.append(-1)
                return
            elif amount / coins[0] != amount // coins[0]:
                Ans.append(-1)
                return
            for i in range(Curr):     
                for j in range(len(coins)):
                    if i + coins[j] > Next:
                        break
                    elif i + coins[j] < Next:
                        continue
                    else: 
                        temp.append(Ans[i]+1)
            Next+=1
            if temp == []:
                Ans.append(0)
            else:
                Ans.append(min(temp))
                M = 1
            return reCur(coins, amount, Ans, Next, M)
                    
        reCur(coins, amount, Ans, 1, 0)
        return Ans[-1]

def coinChange(coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    
    
print(coinChange([186,419,83,408], 6249))