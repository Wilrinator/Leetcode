def addBinary(a, b):
    return format(int(a, 2) + int(b, 2), "b")


def addBinary2(a: str, b: str) -> str:
    A, B = int(a), int(b)
    ans = A + B
    Ans = str(ans)
    for i in range(len(Ans)):
        if Ans[-i-1] == "2" or Ans[-i-1] == "3":
            ans -= 2 * 10 ** i
            ans += 10 ** (i + 1)
            Ans = str(ans)
    return str(ans)




print(addBinary("11","1"))
print(addBinary(a = "1010", b = "1011"))