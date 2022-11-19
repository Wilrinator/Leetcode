def balancedStringSplit(self, s: str) -> int:
    ans = count = 0
    for ch in s:
        count += 1 if ch == 'R' else -1
        if count == 0:
            ans += 1
    return ans

def balancedStringSplit(self, s: str) -> int:
    R, L, count = 0, 0, 0
    for i in range(len(s)):
        if s[i] == "R":
            R += 1
        else:
            L += 1
        if R == L:
            R, L = 0, 0
            count += 1
    return count