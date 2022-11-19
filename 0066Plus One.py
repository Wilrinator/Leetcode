def plusOne(digits: list[int]) -> list[int]:
    digits[-1] += 1
    for i in range(len(digits)):
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
            return digits
        if digits[-i - 1] != 10:
            return digits
        else:
            digits[-i - 1] = 0
            digits[-i - 2] += 1


print(plusOne([9]))