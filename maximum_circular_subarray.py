class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.Kodane(A)
        circ_sum = 0
        for i in range(len(A)):
            circ_sum += A[i]
            A[i] *= -1
        circ_sum += self.Kodane(A)
        if circ_sum > k and circ_sum != 0:
            return circ_sum
        return k

    def Kodane(self, array):
        current_sum, max_sum = array[0], array[0]
        for i in range(1, len(array)):
            current_sum = max(array[i], current_sum + array[i])
            max_sum = max(current_sum, max_sum)
        return max_sum
