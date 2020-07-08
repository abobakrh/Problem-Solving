class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n < 3:
            return res
        nums.sort()
        for i in range(n-2):
            # print("i :: {}".format(i))
            # print("checking for duplicates .... ")
            if nums[i] != nums[i-1] or i == 0:
                # print("not same as previous")
                j = i + 1
                k = n - 1
                # print("j :: {} ,, k :: {}".format(j,k))
                while j < k:
                    # print("i {} ,, j {} ,, k {}".format(i,j,k))
                    summ = nums[i] + nums[j] + nums[k]
                    # print("summing {} , {} , {} = {}".format(nums[i],nums[j],nums[k],summ))
                    if summ == 0:
                        res.append([nums[i],nums[j],nums[k]])
                        while j < k and nums[j] == nums[j+1] :
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1
                    elif summ > 0:
                        k -= 1
                    else:
                        j += 1
        return res