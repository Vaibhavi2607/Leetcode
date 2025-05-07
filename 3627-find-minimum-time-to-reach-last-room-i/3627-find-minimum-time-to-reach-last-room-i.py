class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        INF = float('inf')
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]  # (current_time, x, y)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            cur_time, x, y = heapq.heappop(heap)

            # Early skip if a better time is already recorded
            if cur_time > dist[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    # Move cost is max of current time and cell's availability, then +1 to move
                    next_time = max(cur_time, moveTime[nx][ny]) + 1
                    if next_time < dist[nx][ny]:
                        dist[nx][ny] = next_time
                        heapq.heappush(heap, (next_time, nx, ny))

        return dist[n - 1][m - 1]