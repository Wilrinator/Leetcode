class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
def largestNumber(nums: list[int]) -> str:
    ans = ''.join(sorted([str(int) for int in nums], key=LargerNumKey))
    print(ans)
    return '0' if ans[0] == '0' else ans

def largestNumber2(nums: list[int]) -> str:
    if len(nums) == 1:
        return str(nums[0])
    string_ints = [str(int) for int in nums]
    ans = ""
    string_ints.sort()
    string_ints.append("00")
    for i in range(len(nums)):
        if string_ints[i+1][0] == string_ints[i][0]:
            for j in range(i+1, len(nums)):
                for k in range(1, len(string_ints[i])):
                    if string_ints[j][0] > string_ints[i][0]:
                        break
                    if string_ints[j][k] > string_ints[i][k]:
                        string_ints.insert(j, string_ints[i])
                        string_ints.pop(i)
    del string_ints[-1]
    for i in range(len(nums)):
        ans += string_ints[-i - 1]
    return ans


print(largestNumber([3,30,34,5,9]))