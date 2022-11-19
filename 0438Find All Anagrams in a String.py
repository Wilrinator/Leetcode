def permut(nums, step, ans):
            if step == len(nums):
                return ans
            else:
                check = []
                for i in range(len(ans)):
                    for j in range(len(ans[0])+1):
                        temp = ans[i][:]
                        temp = temp[:j] + nums[step] + temp[j:]
                        if temp not in check:
                            check.append(temp)
                return permut(nums, step+1, check)
            
def findAnagrams3(s: str, p: str):
    LS, LP, S, P, A = len(s), len(p), 0, 0, []
    if LP > LS: 
        return []
    for i in range(LP): 
        S, P = S + hash(s[i]), P + hash(p[i])
        print(S,P)
    if S == P: 
        A.append(0)
    for i in range(LP, LS):
    	S += hash(s[i]) - hash(s[i-LP])
    	if S == P: 
            A.append(i-LP+1)
    return A
            
def findAnagrams(s: str, p: str):
        l = len(p)
        p_frequency = [0] * 26
        ss_frequency = [0] * 26
        res = []
        
        for c in p:
            print(c, ord(c))
            p_frequency[ord(c) - 97] += 1
        print(p_frequency)
        
        for c in s[0:l]:
            print(c)
            ss_frequency[ord(c) - 97] += 1
        print(ss_frequency)
            
        if p_frequency == ss_frequency:
            res.append(0)
            
        for i in range(1, len(s) - l + 1):
            ss_frequency[ord(s[i - 1]) - 97] -= 1
            ss_frequency[ord(s[i + l - 1]) - 97] += 1
            
            if p_frequency == ss_frequency:
                res.append(i)
        
        return res
            
print(findAnagrams(s = "cbaeoipcabersdbabacd", p = "abc"))