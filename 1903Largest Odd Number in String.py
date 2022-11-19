def largestOddNumber(self, num: str) -> str:
        if int(num[-1]) % 2 == 1:
            return num
        for i in range(len(num)):
            if int(num[-i-1]) % 2 == 1:
                return num[:-i]
        return ""