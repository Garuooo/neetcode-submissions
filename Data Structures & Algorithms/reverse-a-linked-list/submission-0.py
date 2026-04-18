# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is empty or has reached the end
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        reversed_list = self.reverseList(head.next)

        # Adjust the pointers
        head.next.next = head
        head.next = None

        return reversed_list
