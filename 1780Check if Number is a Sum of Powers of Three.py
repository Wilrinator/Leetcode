def checkPowersOfThree(self, n: int) -> bool:
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    ans = ''.join(reversed(nums))
    ans = str(ans)
    for i in range(len(ans)):
        if ans[i] == "2":
            return False
    return True