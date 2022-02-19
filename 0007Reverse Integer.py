def reverse(x: int) -> int:
    Ans = ""
    if x < 0:
        x *= -1
        Ans += "-"
    X = str(x)[::-1]
    Ans += X
    if abs(int(Ans)) >= 2**31:
        return 0
    return int(Ans)











print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))
#print(reverse(123))