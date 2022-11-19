def integerReplacement(self, n: int) -> int:
    if n <= 3:
        return n - 1
    if n % 2:
        if (n - 1) % 4:
            return 1 + self.integerReplacement(n + 1)
        return 1 + self.integerReplacement(n - 1)
    return 1 + self.integerReplacement(n // 2)



def integerReplacement2(self, n: int, count=0) -> int:
    if n == 1:
        return count
    elif n % 2 == 0:
        return self.integerReplacement(n / 2, count + 1)
    else:
        return min(self.integerReplacement(n + 1, count + 1), self.integerReplacement(n - 1, count + 1))