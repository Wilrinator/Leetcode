def longestCommonPrefix(strs): # Faster
    ans = ""
    common = ""
    short = min(strs, key=len)   # To find shortest length element in the list
    if short == 0:
        return ans
    for i in range(len(short)):  #再來找是否有相同的字
        common += strs[0][i]
        for j in range(len(strs)):
            if common[i] != strs[j][i]:
                return ans
        ans = common
        i+=1
    return common


print(longestCommonPrefix(["flower", "flow", "flight"]))
#print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["ab","a"]))
print(longestCommonPrefix(["","b"]))