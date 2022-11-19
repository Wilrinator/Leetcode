def addDigits(self, num: int) -> int:
    ans, S = str(num), 0
    if len(ans) > 1:
        for i in range(len(ans)):
            S += int(ans[i])
        return self.addDigits(S)
    return num