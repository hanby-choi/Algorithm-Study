# Fizz Buzz
class Solution(object):
    def fizzBuzz(self, n):
        answer = [str(i) for i in range(n+1)]
        for i in range(1, n+1):
            if i % 3 == 0:
                answer[i] = "Fizz"
            if i % 5 == 0:
                answer[i] = "Buzz"
            if i % 15 == 0:
                answer[i] = "FizzBuzz"
        answer.pop(0)
        return answer