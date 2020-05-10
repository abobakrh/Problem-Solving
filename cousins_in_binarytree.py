# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCousins(self, root, x, y):
        x_store = []
        y_store = []
        parent = None
        Depth = 0
        if root == None:
            return False
        self.dfs_search(root, x, y, 0, None, x_store, y_store)
        return (x_store[0][0] == y_store[0][0]) and (x_store[0][1] != y_store[0][1])

    def dfs_search(self, root, x, y, depth, parent, x_st, y_st):
        if root == None:
            return False
        if root.val == x:
            x_st.append((depth, parent))
        if root.val == y:
            y_st.append((depth, parent))
        self.dfs_search(root.left, x, y, depth+1, root, x_st, y_st)
        self.dfs_search(root.right, x, y, depth+1, root, x_st, y_st)
