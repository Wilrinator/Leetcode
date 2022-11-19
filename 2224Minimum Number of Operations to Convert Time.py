def convertTime(current: str, correct: str) -> int:
        ans = int(correct[3:5]) - int(current[3:5])
        ans1 = int(correct[0:2]) - int(current[0:2])
        if ans < 0:
            ans1 -= 1
            ans += 60
        return ans1 + ans // 15 + (ans % 15) // 5 + ans % 5
    
    
print(convertTime("02:30", "04:35"))