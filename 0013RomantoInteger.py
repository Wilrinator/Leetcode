def romanToInt(s):
    sum = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s)):
        for key in roman:
            if key == s[i]:
                sum += roman[key]
    for j in range(len(s)-1):   #羅馬數字的4和9要特別處裡
        if s[j] == "I" and (s[j+1] == "V" or s[j+1] == "X"):
            sum -=2
        elif s[j] == "X" and (s[j+1] == "L" or s[j+1] == "C"):
            sum -= 20
        elif s[j] == "C" and (s[j+1] == "D" or s[j+1] == "M"):
            sum -= 200

    return sum


def romanToInt2(s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i,su=0,0        
        while i<len(s):
            if i+1<len(s) and s[i:i+2] in d:
                su+=d[s[i:i+2]]
                i+=2
            else:
                su+=d[s[i]]
                i+=1
        return su



print(romanToInt("III"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))