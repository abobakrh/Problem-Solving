import math


class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        return self.square_root(num)

    def square_root(self, num):
        start = 0
        end = num
        while start < end:
            mid = (start + end) // 2
            mid_power2 = mid * mid
            if mid_power2 == num:
                return mid
            elif mid_power2 > num:
                end = mid
            else:
                start = mid + 1
        return False
