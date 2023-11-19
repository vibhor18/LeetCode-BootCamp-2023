class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        
        points.sort(key=lambda point: point[1])

        requiredArrows = 1
        currentEnd = points[0][1]
        for start, end in points:
            
            if currentEnd < start:
                requiredArrows += 1
                currentEnd = end

        return requiredArrows