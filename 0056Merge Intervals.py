def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    if len(intervals) == 1:
        return intervals
    else:
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][-1] >= intervals[i + 1][0]:
                intervals.insert(i, [min(intervals[i][0], intervals[i + 1][0]), 
                                     max(intervals[i][-1], intervals[i + 1][-1])])
                del intervals[i + 1]
                del intervals[i + 1]
                continue
            else:
                i += 1
        return intervals