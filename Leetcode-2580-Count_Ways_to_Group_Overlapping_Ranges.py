class Solution:
    def countWays(self, ranges) -> int:
        count, last = 0, -1
        
        for start, end in sorted(ranges, key=lambda x: x[0]):
            if start > last:
                count += 1
            last = max(last, end)
        
        
        return (2**count) % (7+10**9)