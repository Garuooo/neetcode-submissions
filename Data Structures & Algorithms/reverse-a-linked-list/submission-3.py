# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current_node=head
        while current_node:
            next_node=current_node.next
            current_node.next=prev
            prev=current_node
            current_node=zz
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        reversed_node = self.reverseList(head.next)
        print(f"Reversed Node {reversed_node.val}")
        head.next.next=head
        head.next=None
        return reversed_node

        