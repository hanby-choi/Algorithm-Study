# Plus One
class Solution(object):
    def plusOne(self, digits):
        temp = int(''.join(str(s) for s in digits)) + 1
        result = map(int, list(str(temp)))
        return result
    def plusOne2(self, digits):
        n = len(digits)
        digits[-1] += 1
        cur_digit = 2
        while True:
            if digits[-cur_digit + 1] > 9:  
                digits[-cur_digit + 1] = 0
                if n >= cur_digit:
                    digits[-cur_digit] += 1
                    cur_digit += 1
                elif n == cur_digit - 1:
                    digits.insert(0, 1)
                    break
            else:
                break
        return digits
    def plusOne3(self, digits):
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits