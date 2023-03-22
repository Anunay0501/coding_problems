from collections import defaultdict, deque
from typing import List

# Create a weighted graph, and find the minimum distance road connected with the root. Take care of the cycles.
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)

        for c1, c2, d in roads:
            graph[c1].update({c2: d})
            graph[c2].update({c1: d})

        ans, visited = float('inf'), set()
        qu = deque([1])

        while qu:
            node = qu.popleft()
            
            for connected_cities, distance in graph[node].items():
                ans = min(ans, distance)
            
                if connected_cities not in visited:
                    qu.append(connected_cities)
                    visited.add(connected_cities)
        
        
        return ans