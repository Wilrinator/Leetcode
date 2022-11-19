import math

def search(self, nums: List[int], target: int) -> int:      
        if target < nums[0] or target > nums[-1]:
            return -1
        elif target == nums[0]:
            return 0
        else:            
            Min = 0
            Max = len(nums)            
            while Min+1 < Max:
                n = Min + Max
                m = math.floor(n/2)
                if nums[m] < target:
                    Min = m
                elif nums[m] > target:
                    Max = m
                else:
                    return m
        return -1
    
    
print(search([-1,0,3,5,9,12], 3))
print(search([-1,0,3,5,9,12], 2))