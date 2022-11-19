def canPlaceFlowers2(flowerbed: list[int], n: int) -> bool:
    count = 0
    if len(flowerbed) == 1 and flowerbed[0] == 0:
        n -= 1
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            if count > 2:
                n -= (count - 1) // 2
            count = 0
        elif i == 0 and flowerbed[i] == 0:
            count += 2
            continue
        elif i == len(flowerbed) - 1 and flowerbed[i] == 0:
            count += 2
            if count > 2:
                n -= (count - 1) // 2
        else:
            count += 1
    if n <= 0:
        return True
    return False


print(canPlaceFlowers([0,1,0,1,0,0], n = 1))