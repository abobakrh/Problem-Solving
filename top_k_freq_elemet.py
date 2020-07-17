class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        ans = list(set(nums))
        if len(ans) == k:
            return ans
        arr = []
        for num in ans:
            arr.append(nums.count(num))
        print(ans)
        print(arr)
        while len(ans) != k:
            ans.remove(ans[arr.index(min(arr))])
            arr.remove(min(arr))
        return ans