def countPairs(deliciousness: list[int]) -> int:
        check = [2 ** i for i in range(0, 22)]
        seen = {} # dict to store what we've seen - dynamic programming solution for time requirement
        count = 0
        for i in range(len(deliciousness)):
            for j in range(0, len(check)):
                if check[j] - deliciousness[i] in seen:
                    count += seen[check[j] - deliciousness[i]]
            if deliciousness[i] in seen:
                seen[deliciousness[i]] += 1 
            else:
                seen[deliciousness[i]] = 1
                
        return count % (10**9 + 7) # the arbitrary modulo, presumably to reduce the answer size
    
    
print(countPairs([1,3,5,7,9]))
