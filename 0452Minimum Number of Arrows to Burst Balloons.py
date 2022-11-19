def findMinArrowShots(intervals: list[list[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return n
        intervals.sort(key=lambda x: x[1])
        selected = [intervals[0]]
        for i in range(1,n):
            if intervals[i][0] > selected[-1][1]:
                selected.append(intervals[i])

        return len(selected)



def findMinArrowShots2(points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        i = 0
        while i < len(points) - 1:
            print(points)
            if points[i][1] >= points[i+1][0] or points[i][1] >= points[i+1][0]:
                points.insert(i, [min(points[i][0], points[i + 1][0]), 
                                     min(points[i][-1], points[i + 1][-1])])
                del points[i + 1]
                del points[i + 1]
                continue
            else:
                i += 1
        print(points)
        return len(points)
    
    
    
print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))