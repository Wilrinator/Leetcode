def isUgly(self, n: int) -> bool:
    if n < 1:
        return False
    elif n % 2 == 0:
        return self.isUgly(n / 2)
    elif n % 3 == 0:
        return self.isUgly(n / 3)
    elif n % 5 == 0:
        return self.isUgly(n / 5)
    else:
        return n == 1