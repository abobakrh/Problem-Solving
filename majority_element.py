class Solution(object):
    def majorityElement(self, nums):
        max = len(nums)
        if max == 1:
            return nums[0]
        nums.sort()
        return nums[max/2]
