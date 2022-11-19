def increasingTriplet(nums: list[int]) -> bool:
        a = float('inf')
        b = float('inf')
        for i in nums:
            if i <= a:
                a = i
            elif i <= b:
                b = i
            else:
                return True
        return False


import bisect

def increasingTriplet(nums: list[int]) -> bool:
        Rightmost = -1
        poker_slot = []        
        for number in nums:   
            if not poker_slot or poker_slot[Rightmost] < number:
                poker_slot.append(number)            
            else:
                insert_index = bisect.bisect_left(poker_slot, number)
                poker_slot[insert_index] = number        
        if len(poker_slot) >= 3:
            return True
        else:
            return False