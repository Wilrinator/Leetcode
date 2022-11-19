from collections import Counter
def countKDifference(nums: list[int], k: int) -> int:
        cnt = Counter(nums)
        print(cnt)
        return sum(cnt[key] * cnt[key + k]
            for key in sorted(cnt.keys()) if key + k in cnt)




def countKDifference3(nums: list[int], k: int) -> int:
        nums_dict, count = {}, 0
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
            
        print(nums_dict)

        for num in nums:
            if num + k in nums_dict:
                count += nums_dict[num + k]
        return count


def countKDifference2(nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[j] - nums[i]) == k:
                    print("match", abs(k - nums[i]), i, j)
                    count+=1
        return count
    
    
print(countKDifference([7,7,8,3,1,2,7,2,9,5], 6))