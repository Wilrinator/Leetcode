def letterCombinations(digits: str) -> list[str]:
    Ans = []
    if digits == "":
        return Ans
    list = [1,2,3]
    n = len(digits)
    for i in range(n):
        Lists = [[] for g in range(n)]
        Strlist = [int(digits[i]) * 3 + x + 90 for x in list]
        for j in range(len(Strlist)):
            while i == 0:
                A = [chr(Strlist[j])] * 3
                Ans.extend(A)
                break
            while i == 0 and digits[i] == 9:
                A = [chr(Strlist[j])] * 4
                Ans.extend(A)
                break
    return Ans

def lc(digits, letters, level, Ans, val):
    if level == len(digits):
        Ans.append(val)
        return
    for i in letters[digits[level]]:  # 當妳要重複第一項目一遍但第二項目更多遍時，可以用這方法
        # 先0到下一句後重新執行程序，然後1到下一句，2開始時會執行上面的if，然後return到這裡，並沒有跑回最上面
        lc(digits, letters, level + 1, Ans, val+i)

def letterCombinations2(digits: str) -> list[str]:
    letters = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    Ans = []
    if digits == "":
        return Ans
    lc(digits, letters, 0, Ans, "")
    return Ans



def adding(self,out, level, digits, digitMap):
    if level == len(digits):
        return out
    new = []
    for i in out:
        for j in range(len(digitMap[digits[level]])):
            new.append(i + digitMap[digits[level]][j])
    return self.adding(new, level+1, digits, digitMap)       
            
        
def letterCombinations(self, digits: str) -> List[str]:
    if len(digits) == 0:
        return []
    digitMap ={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    return self.adding(digitMap[digits[0]], 1, digits, digitMap)





print(letterCombinations2(digits = "38"))
#print(letterCombinations2(digits = ""))
#print(letterCombinations2(digits = "3"))