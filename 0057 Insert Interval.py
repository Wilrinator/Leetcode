def insert(intervals, newInterval):
    a, b, c = 0, 0, []
    for i in range(len(intervals)):
        if newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][0]:
            c.append(i)
    print("c = ", c)
    if c == []:
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                intervals.insert(i, newInterval)
                return intervals
        intervals.append(newInterval)
    else:
            if intervals[c[0]][0] < newInterval[0]:
                newInterval[0] = intervals[c[0]][0]
            if intervals[c[-1]][1] > newInterval[1]:    
                newInterval[1] = intervals[c[-1]][1]
            intervals.insert(c[-1]+1, newInterval)
            del intervals[c[0]:c[-1]+1]
    return intervals


def insert2(intervals, newInterval):
    newStart = newInterval[0]
    newEnd = newInterval[1]
    res= []
    for i in intervals:       
        if newStart <= i[1] and newEnd >= i[0]:
            newStart = min(newStart,i[0])
            newEnd   = max(newEnd,i[1])               
        else:
            res.append(i)
    res.append([newStart,newEnd])
    return sorted(res)
                
                
print(insert2(intervals = [[3,5],[12,15]], newInterval = [6,7]))
                
print(insert2(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
