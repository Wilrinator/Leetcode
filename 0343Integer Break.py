def integerBreak(self, n: int, ans=1) -> int:
    if n == 3 and ans == 1:
        return 2
    elif n == 2 and ans == 1:
        return 1
    elif n - 5 >= 0:
        return self.integerBreak(n - 3, ans * 3)
    else:
        return ans * n