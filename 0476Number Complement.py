def findComplement(num: int) -> int:
        b = bin(num)[2:]
        c = ""
        for i in b:
            if i == "0":
                c+="1"
            else:
                c+="0"        
        return int(c, 2)