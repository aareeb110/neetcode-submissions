class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = -(x**2 + y**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (distance, x, y))
            else:
                heapq.heappush(heap, (distance, x, y))
        result = []
        for distance, x, y in heap:
            result.append([x, y])
        
        return result