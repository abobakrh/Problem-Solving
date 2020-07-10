"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(nxt_node):
            if nxt_node == None:
                return (None,None)
            nxt = nxt_node.next
            child = nxt_node.child
            head , tail = nxt_node , nxt_node
            if child is not None:
                head , tail = dfs(child)
                nxt_node.next = head
                child.prev = nxt_node
            if nxt is not None:
                tail_copy = tail
                nxt_head , tail = dfs(nxt)
                tail_copy.next = nxt_head
                nxt_head.prev = tail_copy
            nxt_node.child = None
            return nxt_node , tail
        
        l_l , _ = dfs(head) 
        return l_l
            
        