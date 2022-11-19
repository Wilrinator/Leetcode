def minCost(startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
    Ans = 0
    while startPos != homePos:
        print(startPos, homePos, Ans)
        if startPos[0] != homePos[0]:
            if startPos[0] > homePos[0]:
                startPos[0] -= 1
                Ans += rowCosts[startPos[0]]
            else:
                startPos[0] += 1
                Ans += rowCosts[startPos[0]]
        else:
            if startPos[1] > homePos[1]:
                startPos[1] -= 1
                Ans += colCosts[startPos[1]]
            else:
                startPos[1] += 1
                Ans += colCosts[startPos[1]]

    return Ans



print(minCost(startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]))