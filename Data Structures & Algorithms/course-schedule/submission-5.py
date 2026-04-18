class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print(numCourses,prerequisites)
        ## convert into adjaceny list
        courses=defaultdict(list)
        for course in prerequisites:
            if course[0] == course[1]:
                return False
            courses[course[0]].append(course[1])

        if not courses:
            return True

        self.numCourses=numCourses
        self.visited = set()
        self.pending = set()

        def dfs(root):
            if root in self.visited:
                return True

            if self.numCourses <= 0:
                return False

            if root in self.pending:
                return False
            
            self.numCourses -= 1

            self.pending.add(root)

            for prerequisite in courses[root]:
                if prerequisite not in self.visited:
                    if not dfs(prerequisite):
                        return False
            self.visited.add(root)
            self.pending.remove(root)
            return True
        keys=list(courses.keys())
        for key in keys:
            if not dfs(key):
                return False
        return True