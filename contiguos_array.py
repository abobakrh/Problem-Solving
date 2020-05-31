class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = dict()
        sub_arr , count = 0 , 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count += -1
            if count == 0:
                sub_arr = i + 1
            if count in dic:
                sub_arr = max(sub_arr,i - dic[count])
            else:
                dic[count] = i
        return sub_arr
                
            