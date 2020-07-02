# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        queue = []
        queue.append(root)
        while queue:
            nodes = []
            for i in range(len(queue)):
                element = queue.pop(0)
                nodes.append(element.val)
                if element.left != None:
                    queue.append(element.left)
                if element.right != None:
                    queue.append(element.right)
            ans.insert(0,nodes)
        return ans