def generateParenthesis2(n: int, Ans = None) -> list[str]:
    Pare = "()"
    if Ans == None:
        return generateParenthesis2(n - 1, [Pare])
    elif n == 0:
        return Ans
    else:
        count = len(Ans)
        temp = Ans.copy()
        for _ in range(count):
            Ans.extend(temp)
        lo, ParLo, Find, record = 0,0,0,[]
        print(count)
        for j in range(count):  #外層
            for i in range(count):  # 前兩項
                if lo >= count:
                    ParLo = record[lo - count] + 1 # 找下一個位置
                Find = Ans[lo].find(")", ParLo)
                record.extend([Find])
                print(Ans[lo], Find, lo - count, ParLo)
                Ans[lo] = Ans[lo][:Find] + Pare + Ans[lo][Find:]
                lo += 1
        for k in range(count):
            Ans[-k-1] = Ans[-k-1] + Pare
        Ans = set(Ans)
        print("Answer is:", Ans)
        return generateParenthesis2(n-1, list(Ans))

def generateParenthesis3(n: int) -> list[str]:
    def dfs(ans, s, left, right):
        if left == 0 and right == 0:
            ans.append(s)
        if left:
            print(s)
            dfs(ans, s + '(', left - 1, right)
        if right and left < right:
            dfs(ans, s + ')', left, right - 1)
    ans = []
    dfs(ans, '', n, n)

    return ans

def generateParenthesis(n: int) -> list[str]:
    def dfs(curr, to_open, to_close):
        results = []
            # when this condition is True, we know that we generated all opening and closing parentheses
        if 0 == to_open == to_close: return [curr]
            # if there are parentheses to be opened
        if to_open:
                # update the current string with the opening parentheses
                # decrease 1 from counter of parentheses that we still need to open
                # increase 1 to the counter of parentheses that we still need to close
            results.extend(dfs(curr + "(", to_open - 1, to_close + 1))
            # if there are parentheses to be closed
        if to_close:
                # update the current string with the closing parentheses
                # decrease 1 from counter of parentheses that we still need to close
            results.extend(dfs(curr + ")", to_open, to_close - 1))
        return results
    return dfs('', n, 0)






#print(generateParenthesis(1))
print(generateParenthesis(3))
#print(generateParenthesis(3))