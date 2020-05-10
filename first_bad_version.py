# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
first_bad_ver = 0


def isBadVersion(version):
    if version >= first_bad_ver:
        return False
    return True


class Solution(object):
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            middle = (start + end) // 2
            if isBadVersion(middle) and not isBadVersion(middle - 1):
                return middle
            elif isBadVersion(middle - 1):
                end = middle - 1
            else:
                start = middle + 1
