class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # use BFS
        if not n: return True

        # Buold the adjacency list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        queue = deque([(0, -1)]) # (node, parent)
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    if neighbor != parent:
                        return False # cycle detected
                else:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
        return len(visited) == n # check if all nodes are visited