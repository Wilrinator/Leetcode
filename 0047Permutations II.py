def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        def permut(nums, step, ans):
            if step == 0:
                return permut(nums, 1, [[nums[0]]])
            elif step == len(nums):
                return ans
            else:
                check = []
                for i in range(len(ans)):
                    for j in range(len(ans[0])+1):
                        temp = ans[i][:]
                        temp.insert(j, nums[step])
                        if temp not in check:
                            check.append(temp)
                return permut(nums, step+1, check)
        return permut(nums, 0, [])

import itertools
def permuteUnique2(nums: list[int]) -> list[list[int]]:
    return list(set(itertools.permutations(nums)))

print(permuteUnique2([1,1,2]))