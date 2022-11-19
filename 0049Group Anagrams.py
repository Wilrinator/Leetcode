def groupAnagrams(strs: list[str]) -> list[list[str]]:
        ans = {}
        for i in strs:
            print(ans)
            val = str(sorted(list(i)))
            if val in ans:
                ans[val].append(i)
            else:
                ans[val] = [i]
        return list(ans.values())



def groupAnagrams2(strs: list[str]) -> list[list[str]]:
        Strs = []
        Ans = []
        ans = []
        for i in range(len(strs)):
            Strs.append(sorted(strs[i]))
        for j in range(len(Strs)):
            if Strs[j] not in Ans:
                Ans.append(Strs[j])
                ans.append([strs[j]])
            else:
                for k in range(len(Ans)):
                    if Ans[k] == Strs[j]:
                        ans[k].append(strs[j])
        return ans
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))