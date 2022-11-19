def convertToBase7(self, num: int, ans = 0, order = 0, check = 1) -> str:
        if num == 0:
            return str(ans*check)
        elif num < 0:
            num*=-1
            check = -1
        last = num % 7
        ans+=int(last)*10**order
        return self.convertToBase7((num - last)/7, ans, order+1, check)