def canConstruct3(ransomNote: str, magazine: str) -> bool:
        ransomNote = ''.join(sorted(ransomNote))
        magazine = ''.join(sorted(magazine))
        n = 0
        i = 0
        while i < len(ransomNote):
            if n == len(magazine) or magazine[n] > ransomNote[i]:
                return False
            elif magazine[n] == ransomNote[i]:
                i+=1   
                n+=1
            else:
                n+=1                
            
        return True
    

def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        seen = {}
        for i,x in enumerate(magazine):
            if x not in seen:
                seen[x] = 1
            else:
                seen[x]+=1
        for i,x in enumerate(ransomNote):
            if x not in seen:
                return False
            else:
                seen[x]-=1
        return True
    
from collections import Counter 

def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for i in ransomNote:
            if magazine[i] - ransomNote[i] < 0:
                return False
        return True
                
                
def canConstruct1(self, ransomNote: str, magazine: str) -> bool:        
        def helper(r , m):            
            if not r:
                return True            
            if r[0] in m:
                char = r.pop(0)
                m.pop(m.index(char))                
                return helper(r,m)            
            else:
                return False            
        return helper(list(ransomNote) , list(magazine))