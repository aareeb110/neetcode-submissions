class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the graph and in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        
        # Add nodes with in degree 0 to queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Process the queue
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check for cycle
        if len(result) == numCourses:
            return result
        else:
            return []