import bisect

def maxEnvelopes(envelopes) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        print(envelopes)
        poker_slot = []        
        for number in envelopes:            
            if not poker_slot or poker_slot[-1] < number[1]:
                poker_slot.append(number[1])            
            else:
                inser_index = bisect.bisect_left(poker_slot, number[1])
                poker_slot[inser_index] = number[1]      
        return len(poker_slot)



def maxEnvelopes2(envelopes) -> int:
        envelopes.sort(key= lambda x: (x[0], -x[1]))
        lis = []
        for w, h in envelopes:
            left = binarySearch(lis, h)
            print(left, h , lis)
            if left == len(lis):
                lis.append(h)		    
            else:
                lis[left] = h	    
        return len(lis)
    
    
    
def binarySearch(nums, h):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] == h:
            return mid
        if nums[mid] < h:
            l = mid + 1
        else:
            r = mid - 1
    return l
    
print(maxEnvelopes2([[4,5],[4,6],[6,7],[2,3],[1,1]]))