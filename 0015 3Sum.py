def threeSum(nums):
    Ans = set()
    Num = sorted(nums)
    for i in range(len(Num)-2):
        two = i + 1
        three = len(nums) - 1
        while two < three:
            if Num[two] + Num[three] > -1 * Num[i]:
                three -= 1
            elif Num[two] + Num[three] < -1 * Num[i]:
                two += 1
            else:
                Ans.add((Num[i], Num[two], Num[three]))
                two += 1
                three -= 1
    return [list(j) for j in Ans]

def threeSum2(nums):
        nums.sort()
        result = []
        for num1Idx in range(len(nums)-2):
            # Skip all duplicates from left num1Idx>0 ensures this check is made only from 2nd element onwards
            if num1Idx > 0 and nums[num1Idx] == nums[num1Idx - 1]:
                continue
            (num2Idx, num3Idx) = (num1Idx + 1, len(nums) - 1)
            while num2Idx < num3Idx:
                sum = nums[num1Idx] + nums[num2Idx] + nums[num3Idx]
                if sum == 0:
                    # Add triplet to result
                    result.append((nums[num1Idx], nums[num2Idx], nums[num3Idx]))
                    num3Idx -= 1
                    # Skip all duplicates from right
                    while num2Idx < num3Idx and nums[num3Idx] \
                        == nums[num3Idx + 1]:
                        num3Idx -= 1
                elif sum > 0:

                    # Decrement num3Idx to reduce sum value

                    num3Idx -= 1
                else:

                    # Increment num2Idx to increase sum value
                    num2Idx += 1
        return result









#print(threeSum(nums = [-1,0,1,2,-1,-4]))
#print(threeSum(nums = [-2,0,0,2,2]))
#print(threeSum(nums = [-1,0]))
print(threeSum(nums = [-4,-3,-2,-1,0,1,2,-1,3,0,4]))