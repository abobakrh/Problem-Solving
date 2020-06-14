class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst :
            return 0
        adj_mat = collections.defaultdict(list)
        prices = collections.defaultdict(lambda : float('inf'))
        for s , d , c in flights:
            adj_mat[s] += [(d , c)]
        pq = [(src,-1,0)]
        while len(pq) != 0 :
            city , moves , cost = pq.pop(0)
            if city == dst or moves == K :
                continue
            for neigh , price in adj_mat[city]:
                if prices[neigh] > cost + price:
                    prices[neigh] = cost + price
                    pq += [(neigh , moves + 1 , cost + price)]
        if prices[dst] < float('inf'):
            return prices[dst]
        return -1