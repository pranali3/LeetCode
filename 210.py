class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # TC: O(n + pre)

        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        res = []

        # visitCourse = all courses along the curr DFS path
        visitCourse = set()

        def dfs(course):
            if course in visitCourse:
                return False
            if preMap[course] == []:
                return True
            visitCourse.add(course)
            for pre in preMap[course]:
                # if false
                if not dfs(pre):
                    return False
                if pre not in res:
                    res.append(pre)
            # This is to avoid false loop condition since same course can be pre for multiple courses. If it's already in visit, it will give a false cycle (False) in first if condition.
            visitCourse.remove(course)
            preMap[course] = []
            return True

        # if the graph is disconnected, check every node
        for course in range(numCourses):
            # if false
            if not dfs(course):
                return []
            if course not in res:
                res.append(course)
        return res
