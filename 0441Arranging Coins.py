import math

def arrangeCoins(n: int) -> int:
        return int((math.sqrt(8*n+1)-1)//2)

def arrangeCoins(n: int) -> int:
        ans = 0
        for i in range(1, n+3):
            if n < ans:
                return i-2
            else:
                ans+=i