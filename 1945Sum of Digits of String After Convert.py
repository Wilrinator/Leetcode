def getLucky(self, s: str, k: int) -> int:
        if k == 0:
            return int(s)        
        if "a" <= s[0] <= "z":
            ans = ""
            for i in range(len(s)):
                ans += str(ord(s[i]) - 96)
            return self.getLucky(ans, k)
        else:
            ans = 0
            for i in range(len(s)):
                ans += int(s[i])      
            return self.getLucky(str(ans), k-1)