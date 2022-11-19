def superPow(a: int, b: list[int]) -> int:
    B = 0
    for i in range(len(b)):
        B += b[-i - 1] * (10 ** i)
    c, d = a % 1337, B % 1140 # 1337 = 7 * 191, 1140 = 1337 * (1 - 1/7) * (1 - 1/191) # Euler's theory
    return c ** d % 1337



print(superPow(a = 2, b = [3]))
#print(superPow(a = 2, b = [1,0]))
#print(superPow(a = 1, b = [4,3,3,8,5,2]))
print(superPow(a = 2147483647, b = [2,0,0]))