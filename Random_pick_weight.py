class Solution:

    def __init__(self, w: List[int]):
        self.total_sum = 0
        self.sum = []
        for item in w :
            self.total_sum += item
            self.sum.append(self.total_sum)
        # print("total sum is ",self.total_sum)
        # print(self.sum)

    def pickIndex(self) -> int:
        left , right = 0 , len(self.sum)
        # print("left >> {} , right >> {}".format(left,right))
        random_val = self.total_sum * random.random()
        while left < right :
            middle = (left + right) // 2
            # print("mid is ",middle)
            if self.sum[middle] < random_val:
                left = middle + 1
            else:
                right = middle 
            # print("left >> {} , right >> {}".format(left,right))
        return left
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()