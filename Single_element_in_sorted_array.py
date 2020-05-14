class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for num in list(dict.fromkeys(nums)):
            if nums.count(num) == 1:
                return num
