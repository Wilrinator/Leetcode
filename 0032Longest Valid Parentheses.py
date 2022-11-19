def longestValidParentheses(s: str) -> int:
    ss = []
    ss.append(-1)
    ln = 0
    for i in range(len(s)):
        print(i, ss, ln)
        if s[i] == "(":
            ss.append(i)
        else:
            del ss[-1]
            if (len(ss) == 0):
                ss.append(i)
            else:
                if (i - ss[-1]) > ln:
                    ln = i - ss[-1]
    return ln



print(longestValidParentheses(s = "(()))())("))
print(longestValidParentheses(s = "()(())))"))
print(longestValidParentheses(s = "(()(((()"))