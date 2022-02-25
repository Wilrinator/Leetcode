#Question Soruces: https://leetcode.com/problems/two-sum/

## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up 
## to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## You can return the answer in any order.



### At first, I tried to solve this questions without using 2 for loops
def twoSum(A_list, B):
    a = 0
    b = a + 1
    c = 0
    for count in range(len(A_list) ** 2):
        first_num = A_list[a]
        second_num = A_list[b]
        if first_num + second_num == B:
            return [a + c, b + c]
        count += 1
        b += 1
        if b == len(A_list):
            A_list.remove(first_num)
            b = 1 + a
            c += 1
            
            
### However, using 2 for loops are still faster       
def twoSum2(C,A_list,B):
    for count in range(len(A_list)):
        for match in range(count+1, len(A_list)):
            if A_list[count] + A_list[match] == B:
                return (count,match)



### Using dictionary is much faster, and this is the very first time I learned the benefit and speed of using 
### dictionary
def twoSum3(nums,target):
    seen = {}  # empty dictionary
    for index, value in enumerate(nums):
        if target - value in seen:
            return [index, seen[target - value]]
        else:
            seen[value] = index