def isMatch2(s: str, p: str) -> bool:
    print("s,p" , s, " ", p)
    if p == "":
        if s == p: return True
        else: return False
    elif s == "":
        if len(p) == 1: return False
        elif p[1] == "*": return isMatch(s,p[2:])
        else: return False
    elif p[-1] != "*":
        if s[-1] == p[-1] or p[-1] == ".": return isMatch(s[:-1], p[:-1])
        elif s[-1] != p[-1] : return False
    elif p[1] != "*":
        if s[0] == p[0] or p[0] == ".": return isMatch(s[1:], p[1:])
        else: return False


    elif p[-1] == "*" and p[-2] != ".":
        if len(p) > 2:
            if p[-2] == p[-3]:
                if s.rstrip(p[-2]) != s: return isMatch(s.rstrip(p[-2]) + p[-2], p[:-2])
        return isMatch(s.rstrip(p[-2]), p[:-2])
    elif p[1] == "*" and p[0] != ".":
        print("Y")
        if len(p) > 2:
            if p[2] == p[0]:
                if s.lstrip(p[0]) != s: return isMatch(p[0] + s.lstrip(p[0]),p[2:])
            elif p[3] == "*" and p[2] != "." and p[2] != s[1]:
                print("N")
                return isMatch(s,p[2:])
        return isMatch(s.lstrip(p[0]),p[2:])


    elif p[1] == "*" and p[0] == ".":
        print("check")
        if len(p) == 2: return True
        elif p.count(".*") == 1:
            return isMatch(s,p)
        elif p.count(".*") > 1:
            if p[3] == "*": return isMatch(s, p[:2] + p[4:])
            if p[2] == "." and p[3] != "*": return isMatch(s, p[:3] + p[5:])
            for i in range(len(s)):
                print("loop")
                if s[i] == p[2]:
                    if p[4] != "*" and p[3] != ".":
                        if s[i] == p[2] and s[i+1] == p[3]:
                            print(i)
                            return isMatch(s[s.find(s[i+2]):],p[4:])
                    elif p[4] == "*":
                        return isMatch(s[s.find(s[i]):], p[2:])
                    elif p[3] == "." and p[4]!="*":
                        return True

def isMatch(s: str, p: str) -> bool:
    print("s,p" , s, " ", p)
    # 基礎case
    if p == "":
        if s == p: return True
        else: return False
    elif s == "":
        if len(p) == 1: return False
        elif p[1] == "*": return isMatch(s,p[2:])
        else: return False

    #基礎抵銷case
    elif p[-1] != "*":
        if s[-1] == p[-1] or p[-1] == ".": return isMatch(s[:-1], p[:-1])
        elif s[-1] != p[-1]: return False
    elif p[1] != "*":
        if s[0] == p[0] or p[0] == ".": return isMatch(s[1:], p[1:])
        else: return False

    #特別.*case
    while p.count(".*") > 0:
        print("check")
        if len(p) == 2: return True
        elif p.count(".*") == 1: break
        elif p.count(".*") > 1:
            if p.count("*") < len(p)/2:
                temp = ""
                for i in range(len(p)):
                    if p[i] != "*" and p[i+1] != "*":
                        temp += p[i]
                if ".*" is in [: p.rfind(temp) + 1] and ".*" is in [p.rfind(temp):]:
                    return True
                elif "." not in temp:
                    if temp not in s:
                        return False
                else:
                    if s.rfind([:temp.rfind(".")]) + len(temp) - 1 == s.rfind([temp.rfind(".")-1:]):
                        return True
                    else:
                        return False


    #普通case



def isMatch2(s: str, p: str) -> bool:
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    dp[0][0] = True
    for i in range(1, len(p) + 1):
        dp[i][0] = dp[i - 2][0] if p[i - 1] == "*" else False
    for i in range(len(p)):
        for j in range(len(s)):
            if p[i] == s[j] or p[i] == '.':
                dp[i + 1][j + 1] |= dp[i][j]
            if p[i] == '*':
                if (p[i - 1] == '.' or p[i - 1] == s[j]):
                    dp[i + 1][j + 1] |= dp[i + 1][j] or dp[i][j + 1]
                dp[i + 1][j + 1] |= dp[i - 1][j + 1]

    return dp[-1][-1]





#print(isMatch(s = "aa", p = "a"))
#print(isMatch(s = "aa", p = "a*"))
#print(isMatch(s = "ab", p = ".*"))
#print(isMatch(s = "aaa", p = "aaaa"))
#print(isMatch(s = "mississippi", p = "mis*is*p*."))
#print(isMatch(s = "a", p = "..*"))
#print(isMatch("bbbba", ".*a*a"))
#print(isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"))
#print(isMatch("ab", ".*.."))
print(isMatch("abcaaaaaaabaabcabac" , ".*ab.a.*a*a*.*b*b*"))