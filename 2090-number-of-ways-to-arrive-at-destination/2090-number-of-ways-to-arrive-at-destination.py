class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        
        heap = [(0, 0)]
        while heap:
            d, u = heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    ways[v] = ways[u]
                    heappush(heap, (dist[v], v))
                elif dist[u] + w == dist[v]:
                    ways[v] += ways[u]
        
        return ways[n - 1] % mod
        