class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            bisect.insort(nums,target)
            return nums.index(target)
        