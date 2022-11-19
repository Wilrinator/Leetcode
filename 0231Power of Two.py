def isPowerOfTwo(self, n: int) -> bool:
    if n == 1:
        return True
    elif n <= 0 or n % 2 == 1:
        return False
    elif 0 < n < 1:
        return self.isPowerOfTwo(1 / n)
    else:
        return self.isPowerOfTwo(n / 2)