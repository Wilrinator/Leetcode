def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dic = {}
        for i,n in enumerate(numbers):
            if (target-n) in dic:
                return  [dic[target-n]+1, i+1]
            else:
                dic[n] = i


def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            Sm = numbers[start] + numbers[end]
            if Sm == target:
                return [start+1, end+1]
            elif Sm < target:
                start+=1
            else:
                end-=1