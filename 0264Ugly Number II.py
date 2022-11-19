import heapq
def nthUglyNumber(n: int) -> int:
    if n == 1:
        return 1
    h = [1]
    mul = [2, 3, 5]
    seen = set([1])
    res = []
    while len(res) <= n:
        cur = heapq.heappop(h)
        res.append(cur)
        print(cur, res)
        for m in mul:
            if cur * m not in seen:
                seen.add(cur*m)
                heapq.heappush(h, cur * m)
    return res[n-1]



Ans = [1,2,3,4,5]   
def nthUglyNumber2(n: int, ans = 1, check = [2,2,2], pos = [1,1,1]) -> int:
    if  n <= len(Ans):
        return Ans[n-1]
    else:
        ans = min(2*check[0], 3*check[1], 5*check[2])
        print(Ans, check)
        if ans not in Ans:
            Ans.append(ans)
        if ans == 2*check[0]:
            pos[0]+=1
            check[0] = Ans[pos[0]]
        elif ans == 3*check[1]:
            pos[1]+=1
            check[1] = Ans[pos[1]]
        else:
            pos[2]+=1
            check[2] = Ans[pos[2]]
        return nthUglyNumber2(n, ans, check, pos)
    
print(nthUglyNumber(10))