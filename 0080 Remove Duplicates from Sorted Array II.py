def removeDuplicates(nums) -> int:
        a,b, end = 0, 1, len(nums)
        if end < 3:
            return end
        while b < end:
            if nums[a] == nums[b]:
                if b - a > 1:
                    nums.pop(b)
                    end-=1
                else:
                    b+=1
            else:
                a = b
                b+=1            
        return end