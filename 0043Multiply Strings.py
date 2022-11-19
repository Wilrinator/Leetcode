def multiply(num1: str, num2: str) -> str:
    l1, l2 = len(num1), len(num2)
    i, j, ans = 1, 1, 0
    while i < l1 + 1 and j < l2 + 1:
        ans += int(num1[-i]) * int(num2[-j]) * 10 ** (i + j - 2)
        print(i, j, ans)
        i += 1
        if i > l1:
            i = 1
            j += 1
    return str(ans)


#print(multiply("2", "3"))
print(multiply(num1 = "123", num2 = "456"))