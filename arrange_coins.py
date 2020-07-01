class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        copy = n
        ans = 0
        for i in range(1,n+1):
            if copy >= i:
                copy -= i
                ans += 1
            else:
                return ans
            
        