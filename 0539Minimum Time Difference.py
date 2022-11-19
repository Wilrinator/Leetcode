def findMinDifference(timePoints: list[str]) -> int:
        ans = []
        for i in range(len(timePoints)):
            temp = int(timePoints[i][-2:])
            temp += int(timePoints[i][0:2]) * 60                
            ans.append(temp)
        ans.sort()
        mini = 720
        for i in range(len(timePoints)-1):
            if ans[i+1] - ans[i] == 0:
                return 0
            elif ans[i+1] - ans[i] < 720:
                mini = min(ans[i+1] - ans[i], mini)
            else:
                mini = min(1440 - ans[i+1] + ans[i], mini)
        mini = min(1440 - ans[-1] + ans[0], mini)
        return mini
    
    
print(findMinDifference(["23:59","00:00"]))