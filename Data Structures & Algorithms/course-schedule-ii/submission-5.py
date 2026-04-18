class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses=defaultdict(list)
        ## create adjanceny list
        for preq in prerequisites:
            courses[preq[0]].append(preq[1])
        
        self.visited=list()
        self.pending=set()
        self.order=[]
        def dfs(root):
            if root in self.pending:
                return False
            
            if root in self.visited:
                return True

            self.pending.add(root)


            for children in courses[root]:
                if not dfs(children):
                    return False

            self.pending.remove(root)
            self.visited.append(root)
            return True

        for key in range(numCourses):
            print(self.visited)
            if not dfs(key):
                return []
        return self.visited