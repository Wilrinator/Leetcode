import bisect

def lengthOfLIS(nums: list[int]) -> int:        
        Rightmost = -1
        poker_slot = []        
        for number in nums:         
            print(poker_slot, number)   
            if not poker_slot or poker_slot[Rightmost] < number:
                poker_slot.append(number)            
            else:
                insert_index = bisect.bisect_left(poker_slot, number)
                poker_slot[insert_index] = number        
        return len(poker_slot)











def lengthOfLIS2(nums: list[int]) -> int:
        ans = [1]        
        for i in range(1,len(nums)):
            temp = 0
            for j in range(i):
                print(i,j,ans)
                if nums[i] > nums[j]:
                    temp = max(temp, ans[j])
            ans.append(temp+1)        
        return ans
    
print(lengthOfLIS2([10,9,2,5,3,7,101,18]))