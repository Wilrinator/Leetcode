def mySqrt2(x: int) -> int:
    for i in range(1, x + 2):
        if i ** 2 > x:
            return i - 1


def mySqrt(num: int) -> int:
    start = 0
    end = num
    while start <= end:
        mid = start+(end-start)//2
        print(start, mid, end)
        if mid*mid == num:
            root = mid
            break
        if mid*mid > num:
            end = mid-1
        else:
            start = mid+1
            root = mid
    return root


print(mySqrt(1321))