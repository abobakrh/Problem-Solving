# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        is_odd = True
        odd_list = ListNode(0)
        odd_head = odd_list
        even_list = ListNode(0)
        even_head = even_list
        while head:
            if is_odd:
                odd_list.next = head
                odd_list = odd_list.next
            else:
                even_list.next = head
                even_list = even_list.next
            is_odd = not is_odd
            head = head.next
        even_list.next = None
        odd_list.next = even_head.next
        return odd_head.next
