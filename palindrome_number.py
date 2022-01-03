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

#Without using string conversion
def is_palindrome(x):
    
    if x < 0:
        return False
    
    number = x
    reverse = 0
    while number:
        reverse = reverse * 10 + number % 10
        number //= 10
        print(number)
    return x == reverse

print(is_palindrome(1221))

#How the above example works
# 1st iteration of while loop =>  0 * 10 + 1221 % 10 = 1
# 1221 //= 10 is 122

# 2nd iteration of while loop =>  1 * 10 + 122 % 10 = 12
# 122 //= 10 is 12

# 3rd iteration of while loop =>  12 * 10 + 12 % 10 = 122
# 12 //= 10 is 1

# 4th iteration of while loop =>  122 * 10 + 1 % 10 = 1221
# 1 //= 10 is 0

#Loop breaks and return condition is True


