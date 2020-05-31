# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.in_order_traversal(root)[k-1]
        
        
    def in_order_traversal(self,root):
        # print("*"*25)
        # print("recursion")
        if root == None :
            return []
        left = self.in_order_traversal(root.left)
        root_item = [root.val]
        right = self.in_order_traversal(root.right)
        # print("left is {} -- root is {} -- right is {}".format(left,root_item,right))
        return left + root_item + right
            
        