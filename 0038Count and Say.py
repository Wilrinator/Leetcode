def countAndSay(n: int, ans = "") -> str:
    if n == 0:
        print("n", n)
        return ans
    elif ans == "":
        return countAndSay(n-1,"1")
    else:
        temp = ""
        i, j, count = 0, 0, 1
        while i < len(ans):
            j = i + 1
            print(i, j)
            if i == len(ans) - 1 or j == len(ans):
                temp += str(count) + ans[i]
                print(n,temp)
                return countAndSay(n-1, temp)
            while j < len(ans):
                if ans[j] == ans[i]:
                    count += 1
                    j += 1
                else:
                    temp += str(count) + ans[i]
                    i = j-1
                    break
            i += 1
    print(n, temp)
    return countAndSay(n-1, temp)












#print(countAndSay(1))
print(countAndSay(3))
#print(countAndSay(3))
#print(countAndSay(4))
