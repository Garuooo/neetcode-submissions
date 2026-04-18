# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove_node(node: ListNode, n: int) -> int:
            if not node:
                return 0
            index = remove_node(node.next, n) + 1
            if index == n + 1:
                node.next = node.next.next
            return index
        
        dummy = ListNode(0, head)
        remove_node(dummy, n)
        return dummy.next


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = node = ListNode()
        dummy.next=head
        left,right=dummy,head
        while n > 0:
            n-=1
            right=right.next
        
        while right:
            right=right.next
            left=left.next

        left.next=left.next.next
        return dummy.next


