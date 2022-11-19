import heapq

def nthSuperUglyNumber(n: int, primes: list[int]) -> int:
        nums = primes[:] # do a deep copy 
        heapq.heapify(nums) #create a heap
        p = 1
        for i in range(n - 1):
            print(nums)
            p = heapq.heappop(nums) #take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime) #add all those multiples with the smallest number
                print(p * prime)
                if p % prime == 0:
                    break
        return p

def nthSuperUglyNumber2(n: int, primes: list[int]) -> int:
        m = len(primes)
        pos = [1 for i in range(m)]
        Ans = {1: 1}
        for k in range(n):
            print(Ans, pos)
            ans = min([Ans[pos[i]]*primes[i] for i in range(m)])
            if ans not in Ans:
                Ans[k+2] = ans
            for j in range(m):
                if ans == Ans[pos[j]]*primes[j]:
                    pos[j]+=1
        
        return Ans[n]
    
    
    
print(nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))