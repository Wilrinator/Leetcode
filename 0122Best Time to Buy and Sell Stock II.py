def maxProfit(self, prices: list[int]) -> int:
    ans, i, n = 0, 0, len(prices)
    while i < n - 1:
        j = i + 1
        while j < n:
            if prices[j] > prices[i]:
                if j == n - 1 or prices[j] > prices[j + 1]:
                    ans += prices[j] - prices[i]
                    i = j
                    break
                else:
                    j += 1
            else:
                i = j
                j += 1
    return ans

print(maxProfit([3,3,5,0,0,3,1,4]))