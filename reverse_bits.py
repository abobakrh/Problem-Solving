class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        # print("ans at start = {}".format(bin(ans)))
        for i in range(32):
            ans <<= 1
            # print("ans is {}".format(bin(ans)))
            # print("checking last bit ...")
            if n & 1 == 1:
                # print("last bit is 1")
                ans += 1
                # print("ans is now {}".format(bin(ans)))
            n >>= 1
            # print("right shift n {}".format(bin(n)))
        return ans