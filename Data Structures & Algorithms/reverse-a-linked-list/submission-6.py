# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head.val)
            head=head.next
        reversed_head = itr = ListNode()
        for i in range(len(nodes)-1,-1,-1):
            itr.next=ListNode(nodes[i])
            itr=itr.next
        return reversed_head.next