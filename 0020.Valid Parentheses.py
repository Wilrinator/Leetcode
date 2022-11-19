def isValid(Par) -> bool:
    i = 0
    Par = Par.replace(" ","")
    if Par == "":
        return True
    if Par[-1] == "(" or Par[-1] == "[" or Par[-1] == "{":
        return False
    if Par[0] == ")" or Par[0] == "}" or Par[0] == "]":
        return False
    if len(Par)%2 == 1:
        return False
    while i < len(Par):
        if Par[i] == "(":
            if Par[i+1] == "}" or Par[i+1] == "]":
                return False
            elif Par[i+1] == ")":
                Par = Par[:i] + Par[i+2:]
                if Par=="":
                    return True
                i = 0
                continue
            else:
                return False
        elif Par[i] == "{":
            if Par[i + 1] == ")" or Par[i + 1] == "]":
                return False
            elif Par[i + 1] == "}":
                Par = Par[:i] + Par[i+2:]
                if Par=="":
                    return True
                i = 0
                continue
        elif Par[i] == "[":
            if Par[i+1] == "}" or Par[i+1] == ")":
                return False
            elif Par[i+1] == "]":
                Par = Par[:i] + Par[i+2:]
                if Par=="":
                    return True
                i = 0
                continue
            else:
                return False
        elif Par[i] == ")" or Par[i] == "}" or Par == "]":
            return False
        elif Par[-1] == "(" or Par[-1] == "[" or Par[-1] == "{":
            return False
        i+=1


def isValid2(Par) -> bool:
    Par = Par.strip()
    if Par == "":
        return True
    check = []
    front = ["(","{","["]
    back = [")","}","]"]
    for i in range(len(Par)):
        try:
            if Par[i] in front:   #假如i裡面有前括號，在空白清單內加上對應的下括號
                check.append(back[front.index(Par[i])])
            else:
                if check[-1]==Par[i]:  #如果有相同的下括號，就取消
                    check.pop()
                else:
                    return False
        except IndexError:
            return False

    if check == []:   #當下括號都被清除掉後，便是正確答案
        return True
    else:
        return False




#print(isValid2("({[]})"))
#print(isValid2("()[]{}"))
print(isValid2("(])"))
#print(isValid2("([)]"))
#print(isValid2("{}"))
