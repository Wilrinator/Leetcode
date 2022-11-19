def majorityElement(nums) -> list[int]:
        elem1 = elem2 = None 
        freq1 = freq2 = 0 
        for val in nums:
            if val == elem1:
                freq1 += 1
            elif val == elem2:
                freq2 += 1
            elif freq1 == 0:
                elem1 = val
                freq1 = 1
            elif freq2 == 0:
                elem2 = val 
                freq2 = 1
            else:
                freq1 -= 1
                freq2 -= 1
        
        # at this point, we have two elements with maximum frequency
        # now we need to check the frequency of these two elements, if the particular elements appear more than n//3 times
        count1 = count2 = 0
        for val in nums:
            if val == elem1:
                count1 += 1
            elif val == elem2:
                count2 += 1
        
        res = []
        if count1 > len(nums) // 3:
            res.append(elem1)
        if count2 > len(nums) // 3:
            res.append(elem2)
        return res

from collections import Counter
def majorityElement2(nums) -> list[int]:
        counter = Counter(nums)
        ans = []
        for x in counter:
            if counter[x] > len(nums)/3:
                ans.append(x)
        return ans


def majorityElement3(nums) -> list[int]:
        return [x for x in set(nums) if nums.count(x) > len(nums)/3]
    
    
def majorityElement4(nums) -> list[int]:
    nums.sort()
    n = len(nums)
    k = n//3
    ans = []
    check = [nums[k],nums[min(n-1, k*2 +1)]]
    for i in range(2):
        if nums.count(check[i]) > k:
            if check[i] not in ans:
                ans.append(check[i])
    return ans
    
    
    
print(majorityElement([3,2,2,2,3]))