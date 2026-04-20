# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs recursive 
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs recursive 
        stack = [root]
        while stack:
            current = stack.pop()
            if not current:
                continue
            
            current.left,current.right = current.right,current.left
            stack.append(current.right)
            stack.append(current.left)
        
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if not current:
                continue
            
            current.left,current.right = current.right, current.left
            queue.append(current.left)
            queue.append(current.right)
        
        return root

