"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited={}
        if not node:
            return node
        def iterate(value,neighbors):
            if value in visited:
                return visited[value]
            
            neig_list=[]
            new_node=Node(value,neig_list)
            visited[value]=new_node
            for neighbour in neighbors:
                neig_list.append(iterate(neighbour.val,neighbour.neighbors))
            return new_node
    
        return iterate(node.val,node.neighbors)
