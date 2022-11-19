def __init__(self):
    self.hashMap = {0: 0, 1: 1, 2: 1}


def tribonacci(self, n: int) -> int:
    if n not in self.hashMap:
        self.hashMap[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
    return self.hashMap[n]