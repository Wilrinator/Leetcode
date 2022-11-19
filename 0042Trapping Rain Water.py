def trap(height: list[int], ans = 0) -> int:
    Ans, i = height[:], 0
    while i < len(height) - 2:
        if height[i] == 0:
            i += 1
        j = i + 1
        while j < len(height):
            if height[j] >= height[i]:
                for k in range(i, j):
                    Ans[k] = Ans[i]
                i = j
                break
            elif j == len(height) - 1:
                return trap(height[i:][::-1], sum(Ans) - sum(height))
            else:
                j += 1
    return sum(Ans) - sum(height) + ans



###

# Find maximum height of bar from the left end upto an index i in the array left_max.
# Find maximum height of bar from the right end upto an index i in the array right_max.

# Iterate over the height array and update ans:
# Add min(left_max}[i],right_max}[i]) - height[i] for all i



print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([5,2,0,3,2,4]))