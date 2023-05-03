# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        lower = 1
        upper = n
        while upper > lower:
            mid = lower + (upper - lower) // 2
            if guess(mid) == -1:
                upper = mid - 1
            elif guess(mid) == 1:
                lower = mid + 1
            else:
                return mid
        if upper == lower:
            return upper
