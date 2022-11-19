def bitwiseComplement(n: int) -> int:
        b = bin(n)[2:]
        c = ""
        for i in b:
            if i == "0":
                c+="1"
            else:
                c+="0"        
        return int(c, 2)