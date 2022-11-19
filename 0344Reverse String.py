def reverseString3(s: list[str]) -> None:
    s[:] = s[::-1]

def reverseString2(s: list[str]) -> None:
    n = len(s) - 1

    l, r = 0, n
    while l <= r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

def reverseString(s: list[str], n=1) -> None:
    i, n = 1, len(s)
    while i <= n:
        s.append(s[n-i])
        s.pop(n - i)
        i += 1

print(reverseString(s = ["h","e","l","l","o"]))