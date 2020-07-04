class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        my_set = set()
        heapq.heappush(heap,1)
        while len(heap) > 0 and n > 0:
            possible_nth_ugly = heap[0]
            heapq.heappop(heap)
            n -= 1
            if n == 0:
                return possible_nth_ugly
            for factor in [2,3,5]:
                num = factor*possible_nth_ugly
                if num not in my_set:
                    heapq.heappush(heap,num)
                    my_set.add(num)