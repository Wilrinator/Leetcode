def judgeSquareSum(self, c: int) -> bool:
    low, high = 0, int(c ** 0.5) + 1
    while low <= high:
        tmp = low * low + high * high
        if tmp == c:
            return True
        elif tmp > c:
            high -= 1
        else:
            low += 1
    return False


def judgeSquareSum2(self, c: int) -> bool:
    if ((c ** 0.5) // 1) ** 2 == float(c):
        return True
    ran = int(c ** 0.5 // 1)
    for i in range(ran + 1):
        x = c - i ** 2
        if ((x ** 0.5) // 1) ** 2 == float(x):
            return True
    return False