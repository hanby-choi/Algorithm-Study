class Solution(object):
    def isPalindrome(self, s):
        new = ''
        for c in s:
            if c.isalnum():
                new += c
        new = new.lower()
        mid = int(len(new)/2)
        front = list(new[:mid+1])
        back = list(new[-mid-1:])
        back.reverse()
        if front == back:
            return True
        else:
            return False