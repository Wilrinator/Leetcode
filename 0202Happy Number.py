check = []    
def isHappy(n: int) -> bool:
        if n in check:
            return False
        elif n == 1:
            return True
        check.append(n)
        n, ans = str(n), 0
        l = len(n)
        for i in range(l):
            ans += int(n[i])**2
        return isHappy(ans)
    
print(isHappy(10))