# Questions Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s) -> int:
    if len(s)==0:    # Based case
        return 0
    Ans = []
    Temp = []
    s += s[-1]  # Adding another last character to ensure the Ans will be updated(line 15) before the loop end
    for i in range(len(s)):
        if s[i] not in Temp:   # Adding nont-repeating characters
            Temp += s[i]
        else:
            if len(Ans) <= len(Temp):   # If the next character is repeating
                Ans = Temp
            Temp = Temp[Temp.index(s[i]) + 1:]
            Temp += s[i]
    return len(Ans)








print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("ggububgvfk"))
print(lengthOfLongestSubstring("jbpnbwwd"))
print(lengthOfLongestSubstring("hkcpmprxxxqw"))
