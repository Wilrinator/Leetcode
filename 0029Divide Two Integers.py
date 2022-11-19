def divide(self, dividend: int, divisor: int) -> int:
    if dividend == 2 ** 31:
        if divisor == -1 and abs(divisor) == 1:
            return -(2 ** 31)
        return 2 ** 31 - 1
    elif dividend == -2 ** 31 and abs(divisor) == 1:
        if divisor == -1:
            return 2 ** 31 - 1
        return -(2 ** 31)
    elif dividend % divisor == 0 or dividend * divisor >= 0:
        return dividend // divisor
    else:
        return dividend // divisor + 1