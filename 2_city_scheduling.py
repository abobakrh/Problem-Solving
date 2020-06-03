class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([i for i, j in costs]) + sum(sorted([j - i for i,j in costs])[:len(costs)//2])