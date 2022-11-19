def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    S = ''.join(i for i in s if i.isalnum())
    return S == S[::-1]