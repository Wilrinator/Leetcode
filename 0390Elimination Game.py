def lastRemaining2(self, n: int) -> int:
    if(n == 1):
        return 1        
    return 2 * ((n // 2 - self.lastRemaining(n // 2)) + 1)

def lastRemaining(n: int) -> int:
        N = n   # number of remaining numbers
        fwd = True   # flag for forward/backward elimination
        m = 2    # elimination step/interval
        s = 0   # elimination base

        while N > 1:
            print(s, N, m)
            if fwd or N % 2 == 1: 
                s += m // 2
            m *= 2
            N = N // 2
            fwd = not fwd   # reverse the pass direction
        return s+1
            
            
print(lastRemaining(50))