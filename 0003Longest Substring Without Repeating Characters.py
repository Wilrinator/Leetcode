def lengthOfLongestSubstring(s) -> int:
    if len(s)==0:
        return 0
    Ans = []
    Temp = []
    s += s[-1]
    for i in range(len(s)):
        if s[i] not in Temp:   #加上沒重複的字
            Temp += s[i]
        else:
            if len(Ans) <= len(Temp):   # 取最常沒有重複的字串
                Ans = Temp
            Temp = Temp[Temp.index(s[i]) + 1:]
            Temp += s[i]
    return len(Ans)








print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("ggububgvfk"))
print(lengthOfLongestSubstring("jbpnbwwd"))
print(lengthOfLongestSubstring("hkcpmprxxxqw"))
