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
            
            
            
def twoSum2(C,A_list,B):
    for count in range(len(A_list)):
        for match in range(count+1, len(A_list)):
            if A_list[count] + A_list[match] == B:
                return (count,match)

def twoSum3(nums,target):
    seen = {}  # empty dictionary
    for index, value in enumerate(nums):
        if target - value in seen:
            return [index, seen[target - value]]
        else:
            seen[value] = index