def myAtoi(s: str) -> int:
    s = s.strip()
    if len(s) == 0:
        return 0
    Ans = ""
    if s[0] == "-":
        Ans += "-"
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]
    for i in range(len(s)):
        if "9" >= s[i] >= "0":
            Ans += s[i]
        else:
            break
    try:
        if int(Ans) >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif int(Ans) <= -2 ** 31:
            return -2 ** 31
        return int(Ans)
    except:
        return 0







print(myAtoi("42"))
print(myAtoi("       -42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))
