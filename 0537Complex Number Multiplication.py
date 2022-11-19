def complexNumberMultiply(num1: str, num2: str) -> str:
        real1, real2, im1, im2 = 0, 0, 0, 0
        for i in range(len(num1)):
            if num1[i] == "+":
                real1 = int(num1[:i])
                im1 = int(num1[i+1:-1])
                break
        for i in range(len(num2)):
            if num2[i] == "+":
                real2 = int(num2[:i])
                im2 = int(num2[i+1:-1])
                break
        return str(real1*real2 - im1*im2) + "+" + str(real1*im2 + real2*im1) + "i"