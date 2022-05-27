# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ## Version 1 iteratively
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

        ## Version 2 recursively
        # if not head or not head.next:
        #     return head
        
        # RLH = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return RLH