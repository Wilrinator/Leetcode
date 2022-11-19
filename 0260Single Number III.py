def singleNumber(nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                ans.remove(i)
        return ans