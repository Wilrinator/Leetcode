def constructRectangle(self, area: int) -> list[int]:
        ans = 0
        for i in range(1, int(area**0.5+1)):
            if area % i == 0:
                ans = i                
        return [int(area/ans), ans]