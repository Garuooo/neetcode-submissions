# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])
        while queue:
            last_node = None
            for i in range(len(queue)):
                current = queue.popleft()
                if not current:
                    continue
                last_node = current
                queue.append(current.left)
                queue.append(current.right)
            if last_node:
                res.append(last_node.val)
        
        return res
