def wordBreak5(s: str, wordDict) -> bool:
        wordDict.sort()
        word = [0]
        check = 0
        while check < len(s):
            before = check
            temp = wordDict[:]
            print(check, word)
            for i in temp:
                print(i)               
                if i == s[check:check+len(i)]:
                    word.append(check+len(i))
                    check = word[-1]
                else:
                    continue
            if before == check:
                word.pop()
                if word == []:
                    return False
                check = word[-1]
            
            
                    
        if check == len(s):
            return True
        else:
            return False
        
        
        
        
        
def wordBreak4(s: str, wordDict) -> bool:
        Ans = wordDict[:]     
        
        def reCur(Ans, s, wordDict):
            while Ans != []:
                print(Ans)
                i = 0
                while i < len(Ans):
                    if Ans[i] == s:
                        print(Ans[i])
                        return True
                    elif Ans[i] != s[0:len(Ans[i])]:
                        Ans.pop(i)
                    else:
                        i+=1
                new = []
                for j in Ans:
                    for k in wordDict:
                        new.append(j+k)
                return reCur(new, s, wordDict)
            return False
        return reCur(Ans, s, wordDict)



def wordBreak3(s: str, wordDict) -> bool:
        myset = set(wordDict)
        flag = [-1]*(len(s)+1)        
        def rec(sub):
            size = len(sub)            
            if size == 0:
                return True
            if flag[size] != -1:
                return flag[size]
            for i in range(1,size+1):
                if sub[0:i] in myset:                    
                    print(i, sub[i:])
                    if rec(sub[i:]):
                        print(sub, flag, size)
                        flag[size] = 1
                        return True
            flag[size] =0
            return False                
        return rec(s)



def wordBreak(s: str, wordDict) -> bool:
        def func(idx):
            if idx == len(s):
                return True
            elif dp[idx] != -1:
                return dp[idx]
            func_list = []
            for i in wordDict:
                print(idx, func_list)
                if  s[idx] == i[0] and s[idx:idx+len(i)] == i:
                    func_list.append(func(idx+len(i)))
                else:
                    func_list.append(False)
            dp[idx] = True if sum(func_list) >= 1 else False
            return dp[idx]
        dp = [-1]*len(s)
        return func(0)
           
print(wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
print(wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))