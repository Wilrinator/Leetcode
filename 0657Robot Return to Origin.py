def judgeCircle(moves) -> bool:  #簡單的XY軸
    check = [0,0]
    for i in range(len(moves)):
        if moves[i] == "U":
            check[0]+=1
        elif moves[i] == "D":
            check[0]-=1
        elif moves[i] == "L":
            check[1]-=1
        elif moves[i] == "R":
            check[1]+=1
    if check == [0,0]:
        return True
    else:
        return False

def judgeCircle2(moves: str) -> bool:
    check = ["1"]
    for i in range(len(moves)):
        if moves[i] in check:
            check.pop(check.index(moves[i]))
        elif check[-1] != moves[i]:
            if moves[i] == "U":
                check.append("D")
            elif moves[i] == "D":
                check.append("U")
            elif moves[i] == "L":
                check.append("R")
            elif moves[i] == "R":
                check.append("L")
    if check == ["1"]:
        return True
    else:
        return False







print(judgeCircle2("UD"))
print(judgeCircle2("LL"))
print(judgeCircle2("RRDD"))
print(judgeCircle2("RLUURDDDLU"))