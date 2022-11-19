def floodFill(image, sr: int, sc: int, newColor: int, Next = [[0,0]]):
        print(Next, image)
        OC = image[sr][sc]
        image[sr][sc] = newColor
        if OC == newColor:
            return image
        Next.pop()
        if sr > 0:
            if image[sr-1][sc] == OC and [sr-1,sc] not in Next:
                Next.append([sr-1,sc])
        if sr < len(image)-1:
            if image[sr+1][sc] == OC and [sr+1,sc] not in Next:
                Next.append([sr+1,sc])
        if sc > 0:
            if image[sr][sc-1] == OC and [sr,sc-1] not in Next:
                Next.append([sr,sc-1])
        if sc < len(image[0])-1:
            if image[sr][sc+1] == OC and [sr,sc+1] not in Next:
                Next.append([sr,sc+1])
        if Next == []:
            return image
        else:
            return floodFill(image, Next[-1][0], Next[-1][1], newColor, Next)
        
print(floodFill([[0,0,0],[0,0,0]], 1, 0, 2))