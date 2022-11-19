def fizzBuzz(self, n: int) -> list[str]:
        Ans = []
        for i in range(1, n+1):
            if i%15 == 0:
                Ans.append("FizzBuzz")
            elif i%5 == 0:
                Ans.append("Buzz")
            elif i%3 == 0:
                Ans.append("Fizz")
            else:
                Ans.append("{}".format(i))
        return Ans