# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        for newval in preorder[1:]:
            newval = TreeNode(newval)
            if newval.val < stack[-1].val:
                stack[-1].left = newval
                stack.append(newval)
            else:
                while stack and stack[-1].val < newval.val:
                    stack_top = stack.pop(-1)
                stack_top.right = newval
                stack.append(newval)
        return root

            