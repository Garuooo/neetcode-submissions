"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph={}

        def iterate(node):
            if node in graph:
                return graph[node]

            copy = Node(node.val)
            graph[node]=copy
            for neigh in node.neighbors:
                copy.neighbors.append(iterate(neigh))
            return copy
        return iterate(node) if node else None
