def heightChecker(self, heights: List[int]) -> int:
        check = heights[:]
        heights.sort()
        ans = 0
        for i in range(len(heights)):
            if heights[i] != check[i]:
                ans+=1
        return ans