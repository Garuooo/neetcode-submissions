# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            queue=[root]
            res=[]
            while queue:
                print(queue,res)
                if queue[-1]:
                    res.append(queue[-1].val)
                for i in range(len(queue)):
                    current_node=None
                    while len(queue) > 0 and not current_node:
                        current_node=queue.pop(0)
                    tt = []
                    if current_node:
                        if current_node.left:
                            tt.append(current_node.left)
                        if current_node.right:
                            tt.append(current_node.right)
                        queue=queue+tt
            return res
        return bfs(root)