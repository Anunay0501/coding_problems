import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        conn = [set() for _ in range(n)]

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            conn[a].add(b)

        stck = collections.deque([(-1, 0)])
        ans = 0
        while stck:                         # I chose for sake of my own clarity. Doing dfs is more logical though.
            for _ in range(len(stck)):
                par, node = stck.popleft()
                if par != -1:
                    if par not in conn[node]:
                        ans += 1
                for conn_node in graph[node]:
                    if conn_node != par:
                        stck.append((node, conn_node))
        return ans
