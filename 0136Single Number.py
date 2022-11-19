def singleNumber(nums: list[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
            print(xor)
        return xor





def singleNumber2(nums: list[int]) -> int:
        ans = set()
        notans = set()
        for i in nums:
            if i not in ans:
                ans.add(i)
            else:
                notans.add(i)
        return list(ans - notans)[0]
        
        
        
        
        
print(singleNumber([4,1,2,1,2,4,5,3,3,7,8,5,8]))