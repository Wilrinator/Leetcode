def isPowerOfFour(self, n: int) -> bool:
    if n == 1:
        return True
    elif n <= 0 or n % 4 == 1 or n % 4 == 2 or n % 4 == 3:
        return False
    elif 0 < n < 1:
        return self.isPowerOfFour(1 / n)
    else:
        return self.isPowerOfFour(n / 4)