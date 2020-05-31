class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans = []
        final = []
        for x , y in points:
            ans.append(([x,y],math.sqrt(x**2+y**2)))
        ans.sort(key=lambda tup: tup[1])
        for i in range(K):
            final.append(ans[i][0])
        return final
        
        
        
        