class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        my_map = {}
        ans = cells.copy()
        for i in range(N):
            key = str(ans)
            if key in my_map:
                return self.prisonAfterNDays(ans,( (N - i) % (i - my_map[key]) ))
            else:
                my_map[key] = i
                prev = ans[0]
                for j in range(1,7):
                    curr , nxt = ans[j] , ans[j+1]
                    # ans[j] = 1 - ( (ans[j - 1]) ^ (ans[j + 1]) )
                    ans[j] = 1 - (prev ^ nxt)
                    prev = curr
            ans[0] = 0
            ans[7] = 0
        return ans
                
                
                    
            
        
        
        
        
        
#         l = 8
#         my_dict = {}
#         for i in range(N):
#             my_dict[i] = str(cells)
#             ans = cells.copy()
#             for j in range(1,l-1):
#                 if self.check_Neighbors(j,cells):
#                     ans[j] = 1
#                 else:
#                     ans[j] = 0
#             ans[0] = 0
#             ans[l-1] = 0
#             cells = ans.copy()
#         print(my_dict)
#         return ans
                
                
#     def check_Neighbors(self,cell_index,cells):
#         if cells[cell_index - 1] == cells[cell_index + 1]:
#             return True
#         return False
        