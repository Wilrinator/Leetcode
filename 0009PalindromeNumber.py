def isPalindrome(x: int):
    for i in range(len(str(x))):
        if str(x)[i] != str(x)[-i-1]:
            return False
    return True


def isPalindrome2(x: int):
    return str(x)[::-1] == str(x)





print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))