def findWords(words: list[str]) -> list[str]:
        key = {0: "qwertyuiop", 1: "asdfghjkl", 2: "zxcvbnm"}
        ans = []
        for i in words:
            l = i.lower()
            j = 0
            while j < 3:
                if l[0] in key[j]:
                    count = 0
                    for k in l:    
                        count += 1                  
                        if k not in key[j]:
                            j = 3
                            break
                        elif count == len(l):
                            ans.append(i)
                j+=1
        return ans
    
print(findWords(["Hello","Alaska","Dad","Peace"]))