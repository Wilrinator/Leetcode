def countPrimeSetBits(left: int, right: int) -> int:
    prime = [2, 3 ,5 ,7 , 11, 13, 17, 19]
    count = 0
    for i in range(left, right+1):
        test = bin(i).count('1')        
        if test in prime:
            count+=1
    return count