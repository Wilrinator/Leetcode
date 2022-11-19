def myPow(x: float, n: int, a=0) -> float:
    print(x,n)
    if a == 0:
        a = x
        if n < 0:
            n -= 1
    if n == 0:
        return 1
    elif n == 1 or n == -1:
        return x
    elif n > 0:
        return myPow(x * a, n - 1, a)
    else:
        return myPow(x / a, n + 1, a)


def myPow2(self, x: float, n: int) -> float:
    return x ** n




#print(myPow(2.0,10))
print(myPow(34.00515, -3))



