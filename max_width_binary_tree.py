# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None :
            return 0
        ans = 0
        queue = [[root,0]]
        while queue:
            start_index = queue[0][1]
            end_index = queue[-1][1]
            n = len(queue)
            ans = max(ans,end_index-start_index+1)
            for i in range(n):
                node = queue[0]
                current = node[1] - start_index
                queue.pop(0)
                if node[0].left != None:
                    queue.append([node[0].left, (2*current) + 1])
                if node[0].right != None:
                    queue.append([node[0].right, (2*current) + 2])
        return ans