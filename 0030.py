def findSubstring(s: str, words: list[str]) -> list[int]:
    def rean(A):
        def dfs(ans, s, left, right):
            if left == right:
                ans.append(s + A[left])
            if left < right:
                dfs(ans, s + A[left], left + 1, right)
            if right > left:
                dfs(ans, s + A[right], left, right - 1)

        ans = []
        dfs(ans, '', 0, len(A) - 1)
        return ans

    print(rean(["A", "B", "C"]))


print(findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
print(findSubstring(s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]))