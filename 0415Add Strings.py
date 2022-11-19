def addStrings(num1: str, num2: str) -> str:
    def str_to_int(n):
        integer = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
		# dictionary to map every character to its integer value
        num = 0
        for i in n:
			# traversing the string to add the ones,tens,hundreds of the digit etc
            num = num*10 + integer[i]
        return num
    res = str_to_int(num1)+str_to_int(num2)
    return str(res)




def addStrings2(num1: str, num2: str) -> str:
    carry, rus, ans = 0, 0, ""
    len1, len2 = len(num1), len(num2)
    for i in range(min(len1, len2)):
        carry, rus = divmod(int(num1[-1]) + int(num2[-1]) + carry, 10)            
        ans = str(rus) + ans
        num1 = num1[:-1]
        num2 = num2[:-1]
    if num1 != num2 or carry!=0:
        if len1 > len2:
            for i in range(len(num1)):
                carry, rus = divmod(int(num1[-1]) + carry, 10)
                ans = str(rus) + ans
                num1 = num1[:-1]
                if carry == 0:
                    break
            ans = str(num1) + ans
        elif len1 < len2:
            for i in range(len(num2)):
                carry, rus = divmod(int(num2[-1]) + carry, 10)
                ans = str(rus) + ans
                num2 = num2[:-1]
                if carry == 0:
                    break
            ans = str(num2) + ans                
    if carry!=0:            
        ans = str(carry) + ans
    return ans
    
    
print(addStrings(num1 = "9", num2 = "99"))