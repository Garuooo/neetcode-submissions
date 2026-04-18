# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes={}

        while head:
            if head in nodes:
                return True
            nodes[head]=True
            head=head.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow == fast:
                return True
        return False