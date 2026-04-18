"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.nodes={None: None}

        head3=head
        head2=head
        while head2:
            self.nodes[head2]=Node(head2.val)
            head2=head2.next

        while head3:
            cur = self.nodes[head3]
            if head3.next:
                cur.next= self.nodes[head3.next]
            if head3.random:
               cur.random=self.nodes[head3.random]
            head3=head3.next
        
        return self.nodes[head]