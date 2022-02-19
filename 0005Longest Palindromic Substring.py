def longestPalindrome(s) -> str:
    Ans = ""
    Pal = ""
    ss  = s[::-1]
    for j in range(len(s)):
        if s[j] == ss[j]:
            Pal+=s[j]
            j+=1
            if len(Pal) > len(Ans):
                Ans = Pal
        else:
            Pal = ""
    if Ans == "":
        return s[0]
    return Ans

def longestPalindrome2(s) -> str: #成功解
    Ans = ""
    longest = 0
    j = 0
    if s[::-1] == s:   #把整段迴圈直接轉換成答案，可以省時間
        return s
    for i in range(len(s)):   # 要找最長的迴圈
        j = i+1
        k = i-1
        while k >= 0 and j < len(s) and s[k] == s[j]:   # 我們要設定範圍，所以while比較好用
            length = j-k+1
            if length > longest:
                longest = length
                Ans = s[k:j+1]
            k-=1
            j+=1
    for i in range(len(s)):   #要找偶數長度的迴圈
        j = i+1
        k = i
        while k >= 0 and j < len(s) and s[k] == s[j]:
            length = j-k+1
            if length > longest:
                longest = length
                Ans = s[k:j+1]
            k-=1
            j+=1
    if Ans == "":
        return s[0]
    return Ans






#print(longestPalindrome2("babcc"))
#print(longestPalindrome2("cbbd"))
#print(longestPalindrome2("a"))
#print(longestPalindrome2("eabcb"))
print(longestPalindrome2("aacabdkacaa"))