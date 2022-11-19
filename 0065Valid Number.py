def isNumber(self, s: str) -> bool:
        sign, E, n, dot, num= 0, 0, len(s), 0, 0
        for i in range(n):
            if "A" <= s[i] <= "z":
                if E == 1 or num == 0:
                    return False
                elif s[i] == "E" or s[i] == "e":
                    E+=1
                    sign = 0
                    dot = 0
                    num = 0
                else:
                    return False
            elif s[i] == "+" or s[i] == "-":
                if dot == 1 or sign == 1 or num > 0:
                    return False
                else:
                    sign+=1
            elif s[i] == ".":
                if dot == 1 or E == 1:
                    return False
                else:                    
                    dot+=1
            else:
                num+=1
        if num == 0:
            return False
        elif E == 1 and num == 0:
            return False
        return True