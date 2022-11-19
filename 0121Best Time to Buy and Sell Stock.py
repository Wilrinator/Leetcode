def maxProfit(prices: list[int]) -> int:
    ans, i = 0,0
    while i < len(prices)-1:
        print("i =", i)
        j = i + 1
        if prices[j] > prices[i]:
            while j < len(prices):
                print("j =" , j)
                temp = prices[j] - prices[i]
                if temp > ans:
                    ans = temp
                elif temp < 0:
                    break
                j += 1
        i = j
    return ans


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))