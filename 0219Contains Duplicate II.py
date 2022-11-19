def containsNearbyDuplicate3(nums: list[int], k: int) -> bool:
        # Check if there are no duplicates in the array
        if len(nums) == len(set(nums)):
            return False
        
        i, j, z = 0, 1, 0
        seen = set()  #Track all numbers we've already checked.
        while i < len(nums)-1:
            if (val := nums[i]) in seen:
                i += 1
                j += 1
                continue
            else:
                seen.add(val)
                  
            while j < len(nums):
                if nums[j] == val:
                    if z and abs(j-z) <= k:
                        return True
                    elif abs(j-i) <= k:
                        return True
                    else:
                        z = j  
                j += 1
            
			# Reset our pointers
            i += 1
            j = i+1
            z = 0
            
        return False





def containsNearbyDuplicate(nums: list[int], k: int) -> bool:        
        dic = {}        
        for i in range(0,len(nums)):
            print(i, dic)
            if nums[i] in dic:
                if(abs(dic[nums[i]] - i) <=k ):
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i        
        return False




def containsNearbyDuplicate2(nums: list[int], k: int) -> bool:
        n = len(nums)
        if len(set(nums)) == n:
            return False  
        for i in range(n-1):
            if nums[i:min(i+1+k, n)].count(nums[i]) > 1:
                return True
        return False
    
    
print(containsNearbyDuplicate3([1,2,3,4,5,6,7, 1, 2, 3,8,9,9], 3))