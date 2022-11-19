def singleNumber(nums: list[int]) -> int:
        ans = set()
        notans = set()
        for i in nums:
            if i not in ans:
                ans.add(i)
            else:
                notans.add(i)
        return list(ans - notans)[0]