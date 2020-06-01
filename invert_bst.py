# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        copy = root
        if copy == None:
            return None
        left_leaf = self.invertTree(copy.left)
        right_leaf = self.invertTree(copy.right)
        copy.left = right_leaf
        copy.right = left_leaf
        return copy
