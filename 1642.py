import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff >= 0:
                heapq.heappush(heap, diff)
        return 0