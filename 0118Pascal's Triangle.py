hashMap = {1:[1], 2:[1,1], 3:[1,2,1], 4:[1,3,3,1], 5:[1,4,6,4,1]}


def generate(self, num: int, k=31) -> List[List[int]]:
    n = 5
    while n < k:
        if n not in self.hashMap:
            self.hashMap[n] = [1, 1]
            for i in range(1, n - 1):
                self.hashMap[n].insert(1, self.hashMap[n - 1][i - 1] + self.hashMap[n - 1][i])
        n += 1
    return list(self.hashMap.values())[:num]



print(generate(5))