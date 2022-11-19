def isPowerOfThree(self, n: int) -> bool:
    if n == 1:
        return True
    elif n <= 0 or n % 3 == 1 or n % 3 == 2:
        return False
    elif 0 < n < 1:
        return self.isPowerOfThree(1 / n)
    else:
        return self.isPowerOfThree(n / 3)