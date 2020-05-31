class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a_count , b_count = 0 , 0
        ans = []
        len_a = len(A)
        len_b = len(B)
        while a_count < len_a and b_count < len_b:
            start , end = max(A[a_count][0],B[b_count][0]) , min(A[a_count][1],B[b_count][1])
            if start <= end :
                ans.append([start,end])
            if A[a_count][1] < B[b_count][1] :
                a_count += 1
            else :
                b_count += 1
        return ans
            
        