def isPrefixString(self, s: str, words: list[str]) -> bool:
        if s == "":
            return True
        elif words == []:
            return False
        n = len(words[0])
        if len(s) < n:
            return False
        for i in range(n):
            if s[i] != words[0][i]:
                return False
        return self.isPrefixString(s[n:], words[1:])
    
    
print(isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"]))
    