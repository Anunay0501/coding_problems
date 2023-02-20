from collections import defaultdict
import math


class Solution:
    def minimumFuelCost(self, roads, seats: int) -> int:
        self.ans=0
        self.graph=defaultdict(list)
        
        for a,b in roads:
            self.graph[a].append(b)
            self.graph[b].append(a)
        
        
        def bt(node,par):  
            count=1
            
            for conn_node in self.graph[node]:
                if conn_node != par:
                    count+=bt(conn_node,node)

            if node!=0:
                self.ans+=math.ceil(count/seats)
            return count
        
        bt(0,-1)
        
        return self.ans