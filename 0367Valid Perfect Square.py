def isPerfectSquare2(self, num: int) -> bool:
    return ((num ** 0.5) // 1) ** 2 == float(num)

def isPerfectSquare(self, num: int) -> bool:
    start = 0
    end = num
    while start <= end:
        mid = start + (end - start) // 2
        if mid * mid == num:
            return True
        if mid * mid > num:
            end = mid - 1
        else:
            start = mid + 1
            root = mid
    return False

