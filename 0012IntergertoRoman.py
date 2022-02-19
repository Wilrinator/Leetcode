def intToRoman2(num):
    input = str(num)
    result = ""
    for i in range(len(input)*2):
        if len(input) == 4:    # 千位數
            result += int(input[0]) * "M"
            input = input[1:]
        elif len(input) == 3:   # 百位數
            new_num = int(input)
            if new_num >= 400:
                if 500 > new_num >= 400:
                    result += "CD"
                    input = input[1:]
                elif new_num >= 900:
                    result += "CM"
                    input = input[1:]
                elif new_num >=500:
                    result += "D"
                    new_num -= 500
                    input = str(new_num)
            else:
                result += int(input[0]) * "C"
                input = input[1:]
        elif len(input) == 2:   #十位數
            new_num = int(input)
            if new_num >= 40:
                if 50 > new_num >= 40:
                    result += "XL"
                    input = input[1:]
                elif new_num >= 90:
                    result += "XC"
                    input = input[1:]
                elif new_num >= 50:
                    result += "L"
                    new_num -= 50
                    input = str(new_num)
            else:
                result += int(input[0]) * "X"
                input = input[1:]
        elif len(input) == 1: #個位數
            new_num = int(input)
            if new_num >= 4:
                if 5 > new_num >= 4:
                    result += "IV"
                    input = input[1:]
                elif new_num >= 9:
                    result += "IX"
                    input = input[1:]
                elif new_num >= 5:
                    result += "V"
                    new_num -= 5
                    input = str(new_num)
            else:
                result += int(input[0]) * "I"
                return result
        elif len(input) == 0:
            return result

def intToRoman(n: int) -> str:
    d = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90,  'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4,'I':1}
    s = str() 
    for i, j in d.items(): # Bring from 'M':1000 to 'I':1 one by one
        while True:
            if n >= j: # If n is greater than or equal to j then
                n -= j # Subtract the value from n
                s += i # Add the chracter to s
            else:
                break
    return s


def intToRoman3(num: int) -> str:
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]




#print(intToRoman(3800))
print(intToRoman(4))
#print(intToRoman(79))
#print(intToRoman(1678))
#print(intToRoman(3858))

