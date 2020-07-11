class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            n = len(ans)
            for j in range(n):
                a = ans[j] + [i]
                ans.append(a)
        return ans
        