def fourSum(nums: list[int], target: int) -> list[list[int]]:
    Ans = set()
    Num = sorted(nums)
    for i in range(len(Num)-3):
        for j in range(i+1, len(Num)-2):
            one = i
            two = j
            three = j + 1
            four = len(nums) - 1
            while three < four:
                total = Num[one] + Num[two] + Num[three] + Num[four]
                if total > target: four -= 1
                elif total < target: three += 1
                else:
                    Ans.add((Num[one], Num[two], Num[three], Num[four]))
                    three += 1
                    four -= 1
    return [list(j) for j in Ans]


print(fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(fourSum(nums = [0,0,0,0], target = 0))