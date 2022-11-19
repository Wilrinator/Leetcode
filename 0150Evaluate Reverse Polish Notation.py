def evalRPN(tokens) -> int:
        Notation = ["+", "-", "*", "/"]
        Num = []
        for i in range(len(tokens)):
            print(Num)
            if tokens[i] not in Notation:
                Num.append(int(tokens[i]))
            else:
                Num2 = Num.pop()
                Num1 = Num.pop()
                if tokens[i] == Notation[0]:
                    Num.append(Num1+Num2)
                elif tokens[i] == Notation[1]:
                    Num.append(Num1-Num2)
                elif tokens[i] == Notation[2]:
                    Num.append(Num1*Num2)
                elif tokens[i] == Notation[3]:
                    Num.append(int(Num1/Num2))
        return Num[0]
    
    
    
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))