def wordPattern(pattern: str, s: str) -> bool:
        hash1={}
        hash2={}
        
        for i in range(0,len(pattern)):
            if pattern[i] not in hash1:
                hash1[pattern[i]]=[i]
            else:
                hash1[pattern[i]].append(i)
        lis=s.split(' ')
        for i in range(0,len(lis)):
            if lis[i] not in hash2:
                hash2[lis[i]]=[i]
            else:
                hash2[lis[i]].append(i)
        print(hash1,hash2)

        res1=[]
        res2=[]
        for k,v in hash1.items():
            res1.append(v)
        for k,v in hash2.items():
            res2.append(v)
        print(res1, res2)
        return(res1==res2)





def wordPattern2(pattern: str, s: str) -> bool:
        ans = {}
        l=s.split()
        if len(l) != len(pattern):
            return False
        for i in pattern:
            if i not in ans:   
                print(i, pattern, l, ans)         
                ans[i] = l[0]
                l.pop(0)
            else:
                print(i, pattern, l, ans)
                if ans[i] == l[0]:
                    l.pop()
                    continue
                else:
                    return False
        if len(set(ans.values())) != len(ans):
            return False
        return True
    
print(wordPattern(pattern = "abba", s = "dog cat cat dog"))