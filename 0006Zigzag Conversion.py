def convert(s,numRows)->str:
    Ans = ""
    Seq = 2*numRows-2
    if numRows == 1:  # 把特例去掉
        Seq = 1
    Lists = [[] for g in range(Seq)]  #製造N個清單
    for i in range(len(s)):
        for j in range(Seq):
            Snum = i+1
            Lnum = j+1
            if Snum % Seq == 0:    #把String造著mod的數字排列
                Lists[-1]+=s[i]
                i+=1
            elif Snum % Seq == Lnum:
                Lists[j]+=s[i]
    for a in range(1,numRows-1):     #把中間的清單做出來
        for b in range(len(Lists[-a])):
            Lists[a].insert(b*2+1,Lists[-a][b])
    for l in range(numRows):    #做成一個大清單
        for m in range(len(Lists[l])):
            Ans+=Lists[l][m]
    return Ans

def convert2(s,numRows):
    if numRows == 1:
        return s
    arr = [""] * numRows
    p = 0
    flag = True
    for i in range(len(s)):
        arr[p] += s[i]
        if flag:
            p += 1
        else:
            p -= 1
        if p == numRows - 1:
            flag = not flag
        elif p == 0:
            flag = not flag
    return "".join(arr)





print(convert2("PAYPALISHIRING",3))
print(convert2("PAYPALISHIRING",4))
#print(convert("A",1))
#print(convert())
