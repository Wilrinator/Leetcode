def selfDividingNumbers(left: int, right: int) -> list[int]:
        ans = []
        for i in range(left, right+1):
            for num in str(i):
                if num == "0" or i % int(num) != 0:
                    break
            else:
                ans.append(i)
        return ans



def selfDividingNumbers2(left: int, right: int) -> list[int]:
    ans = []
    for i in range(left, right+1):
        for j in range(len(str(i))):
            if str(i)[j] == "0" or i % int(str(i)[j]) != 0:
                break
            elif j == len(str(i))-1 and i % int(str(i)[j]) == 0:
                ans.append(i)
    return ans
    
    
    
    

print(selfDividingNumbers(left = 1, right = 22))