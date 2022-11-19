def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    if sum(arr) % 3 != 0:
        return False
    else:
        i, Sum, count, check = 0, 0, 0, sum(arr) // 3
        for i in range(len(arr)):
            Sum += arr[i]
            if count == 2 and i != len(arr):
                return True
            elif Sum == check:
                count += 1
                Sum = 0
        return False