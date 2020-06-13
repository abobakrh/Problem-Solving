class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r_count = nums.count(0)
        w_count = nums.count(1)
        b_count = nums.count(2)
        nums.clear()
        nums += [0]*r_count + [1]*w_count + [2]*b_count

            
        
        