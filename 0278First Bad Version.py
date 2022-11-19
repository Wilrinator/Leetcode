def firstBadVersion(n):
        low, high = 1, n
        
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                high = mid			
        return low