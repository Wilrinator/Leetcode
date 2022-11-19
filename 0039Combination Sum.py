def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    ans, curr, n = [], [], len(candidates)
    candidates.sort()
    def dfs(curr, target, idx):
        if target < 0:
            return
        if target == 0:
            ans.append(curr[:])
            return
        for i in range(idx, n):
            print(curr, idx, target, i)
            curr.append(candidates[i])
            dfs(curr, target - candidates[i], i)
            curr.pop()
    dfs([], target, 0)
    return ans


def combinationSum2(candidates: list[int], target: int, temp=[], ans=[], loc=[], n = 0) -> list[list[int]]:
    if n == 0:
        temp,ans,loc = [],[],[]
    if temp != []:
        for i in range(len(temp)):
            for j in range(len(candidates)):
                if temp[i] == candidates[j]:
                    loc[i].append(candidates[j])
                    print(loc, i)
                    ans.append(list(sorted(loc[i])))
                    print(ans)
                    loc[i].pop(-1)
    if temp == []:
        for i in range(len(candidates)):
            temp.append(target)
    for i in range(len(candidates)):
        print(i)
        temp[i] -= candidates[i]
        loc.append([])
        if temp[i] >= 0:
            loc[i].append(candidates[i])
            if temp[i] == 0:
                ans.append(loc[i])
        else:
            candidates = candidates[:i]
            temp = temp[:i]
            break
    for i in range(len(temp)):
        if temp[i] > 0:
            print(loc)
            print(temp)
            print(candidates)
            return combinationSum2(candidates, target, temp, ans, loc, n+1)
    rem = []
    for i in range(len(ans)-1):
        if ans[i] == ans[i+1]:
            rem.append(i)
    for i in range(len(rem)):
        ans.pop(rem[-i])
    return ans














print(combinationSum(candidates = [2,3,5,7], target = 7))
#print(combinationSum(candidates = [2,3,5], target = 8))
#print(combinationSum(candidates = [2,3], target = 1))
#print(combinationSum(candidates = [1], target = 2))