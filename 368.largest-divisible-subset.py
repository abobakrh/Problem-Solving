#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
import bisect


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # if n <= 1:
        #     return nums
        # current = []
        # dp = []
        # hasone = False
        # nums.sort()
        # if nums[0] == 1:
        #     hasone = True
        #     nums.remove(1)
        #     n -= 1
        # for i in range(n):
        #     arr = [nums[i]]
        #     for j in range(i+1, n):
        #         # print("i :: {} ,, j :: {}".format(i, j))
        #         if nums[j] % arr[-1] == 0 :
        #             arr.append(nums[j])
        #         dp.append(arr)
        # max = 0
        # for index,li in enumerate(dp):
        #     if len(dp[index]) > max:
        #         current = li
        #         max = len(dp[index])
        # if hasone :
        #     bisect.insort(current,1)

        # # print(dp)
        # # print(trace)
        # # print(current)

        # return current
        if len(nums) == 0:
            return []
        nums.sort()
        result = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(result[i]) <= len(result[j]):
                    result[i] = result[j] + [nums[i]]
        return max(result,key=len)


# @lc code=end
