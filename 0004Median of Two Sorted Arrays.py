def findMedianSortedArrays(l1,l2):
    list = sorted(l1 + l2)
    if len(list) % 2 == 1:
        return list[len(list)//2]
    else:
        return (list[len(list)//2]+list[len(list)//2-1])/2


print(findMedianSortedArrays([1,3],[2]))
print(findMedianSortedArrays([],[2]))
print(findMedianSortedArrays([2],[1]))