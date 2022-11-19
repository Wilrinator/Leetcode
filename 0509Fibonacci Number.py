class Solution:
    def __init__(self):
        self.hashMap = {0: 0, 1: 1, 2: 1}
    def fib(self, n: int) -> int:
        if n not in self.hashMap:
            self.hashMap[n] = self.fib(n-1) + self.fib(n-2)
        return self.hashMap[n]