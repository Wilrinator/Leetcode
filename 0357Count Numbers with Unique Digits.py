def __init__(self):
        self.hashMap = {0: 1, 1: 10, 2: 91}
def countNumbersWithUniqueDigits(self, n: int) -> int:
    ans = 9
    for i in range(n-1):
        ans*= (9-i)
    if n not in self.hashMap:
        self.hashMap[n] = self.countNumbersWithUniqueDigits(n-1) + ans
    return self.hashMap[n]