def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): #Checking the lengths 
            return False

        for i,j in zip(sorted(set(s)),sorted(set(t))):
            if s.count(i)==t.count(j) and i==j: 
                continue
            else:
                return False                
        return True




def isAnagram(self, s: str, t: str) -> bool:
        word_dict1, word_dict2, count = {}, {}, 0
        for letter in s:
            if letter not in word_dict1:
                word_dict1[letter] = 1
            else:
                word_dict1[letter] += 1
        for letter in t:
            if letter not in word_dict2:
                word_dict2[letter] = 1
            else:
                word_dict2[letter] += 1
        return word_dict1 == word_dict2