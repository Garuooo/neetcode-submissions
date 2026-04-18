# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        queue = [root]
        while queue:
            rightSide=None
            for i in range(len(queue)):
                current_node= queue.pop(0)
                if current_node:
                    queue=queue+[current_node.left,current_node.right]
                    rightSide=current_node
                
            if rightSide:
                res.append(rightSide.val)


        return res