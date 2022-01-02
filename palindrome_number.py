# Original string version
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        ls = [int(n) for n in str(x)]
        start = 0
        end = len(ls) - 1

        while True:

            if ls[start] == ls[end]:
                if start == end or end < start:
                    return True
                start = start + 1
                end = end - 1

            else:
                return False