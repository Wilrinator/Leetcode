def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
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
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            curr.append(candidates[i])
            dfs(curr, target - candidates[i], i)
            curr.pop()
    dfs([], target, 0)
    return ans




print(combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
#print(combinationSum2(candidates = [2,5,2,1,2], target = 5))
