def maximumDifference(self, prices: list[int]) -> int:
    ans, i = 0, 0
    while i < len(prices) - 1:
        j = i + 1
        if prices[j] > prices[i]:
            while j < len(prices):
                temp = prices[j] - prices[i]
                if temp > ans:
                    ans = temp
                elif temp < 0:
                    break
                j += 1
        i = j
    if ans == 0:
        return -1
    return ans