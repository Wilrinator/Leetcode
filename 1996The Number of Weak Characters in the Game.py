def numberOfWeakCharacters3(properties) -> int:        
        properties.sort(key=lambda x: (x[0], -x[1]))        
        stack = []
        ans = 0        
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans


def numberOfWeakCharacters2(properties) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))
        curY = 0
        count = 0
        for x,y in properties:
            if y < curY:
                count+=1
            else:
                curY = y
        return count


def numberOfWeakCharacters(properties) -> int:
        properties.sort(key = lambda x: (-x[0], +x[1]))
        print(properties)
        count = 0
        i = 0
        while i < len(properties)-1:
            if properties[i+1][1] < properties[i][1]:
                count+=1
                del properties[i+1]
            else:
                i+=1
        print(properties, count)
        return count 
    
print(numberOfWeakCharacters3([[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]))