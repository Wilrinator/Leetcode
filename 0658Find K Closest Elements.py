def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
        if k == len(arr):
            return arr        
        if x <= arr[0]: 
            return arr[:k]			
        if x >= arr[-1]: 
            return arr[-k:]
        
        low, high = 0, len(arr)-1
        while low+1 < high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid
            elif arr[mid] >= x:
                high = mid	
        ans, left, right = [], low, low+1
        while len(ans) < k:
            if right == len(arr) or abs(x - arr[left]) <= abs(x - arr[right]):
                ans.append(arr[left])
                left-=1
            elif left == -1 or abs(x - arr[left]) > abs(x - arr[right]):
                ans.append(arr[right])
                right+=1
        ans.sort()
        return ans







print(findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))




