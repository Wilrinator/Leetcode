def binaryGap(n: int) -> int:
        gaps, end, j, i = 0, 0, 0, 0
        n = bin(n)[2:]
        if n.count("1") == 1:
            return 0
        while j < len(n):
            if n[j] == "1":
                for i in range(j+1, len(n)):
                    if n[i] == "1":
                        end = i
                        break
                gaps = max(gaps, end-j)     
            j = max(i, j+1)
        return gaps
    
print(binaryGap(13))