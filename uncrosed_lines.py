class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_a , len_b = len(A) , len(B)
        # print("len of a is ",len_a)
        # print("len of b is ",len_b)
        dynamic_arr = [ [0 for _ in range(len_b + 1)] for _ in range(len_a + 1) ]
        for i in range(1,len_a+1):
            for j in range(1,len_b+1):
                # print("{} :: {} ?".format(A[i-1],B[j-1]))
                if A[i-1] == B[j-1]:
                    # print("equal")
                    dynamic_arr[i][j] = dynamic_arr[i-1][j-1] + 1
                else :
                    # print("not equal")
                    dynamic_arr[i][j] = max(dynamic_arr[i-1][j],dynamic_arr[i][j-1])
        # print("*"*25)
        # for i in dynamic_arr:
        #     print(i)
        return dynamic_arr[len_a][len_b]
                    
                
                
        
        