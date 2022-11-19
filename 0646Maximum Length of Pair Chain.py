def findLongestChain(pairs) -> int:
        pairs.sort()
        rt = 1
        l = pairs[0]
        for r in range(1,len(pairs)):
            print(l, pairs[r], rt)
            if l[1] < pairs[r][0]:
                rt += 1 
                l = pairs[r]
            elif pairs[r][1] < l[1]:
                l = pairs[r]
        return rt 

import operator
def findLongestChain2(pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            print(x,y)
            if cur < x:
                cur = y
                ans += 1
        return ans


def findLongestChain3(pairs: list[list[int]]) -> int:
        pairs.sort()
        ans = [1]
        for i in range(1, len(pairs)):
            temp = 0
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    temp = max(temp, ans[j])
            ans.append(temp+1) 
        return max(ans)
    
print(findLongestChain2([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))