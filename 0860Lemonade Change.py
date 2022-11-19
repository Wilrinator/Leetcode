def lemonadeChange(bills: list[int]) -> bool:
    cash = [0, 0]
    for i in range(len(bills)):
        if cash[0] < 0:
            return False
        if bills[i] == 5:
            cash[0] += 1
        else:
            if bills[i] == 10:
                cash[0] -= 1
                cash[1] += 1
            else:
                if cash[1] > 0:
                    cash[0] -= 1
                    cash[1] -= 1
                else:
                    cash[0] -= 3
    if cash[0] < 0 or cash[1] < 0:
        return False
    return True

print(lemonadeChange([5,5,5,5,20,20,5,5,5,5]))