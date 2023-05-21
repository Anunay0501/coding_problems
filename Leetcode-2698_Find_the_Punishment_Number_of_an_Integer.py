class Solution:
    def punishmentNumber(self, n: int) -> int:        
        arr = [0]*(n+1)
        
        def squareSumCheck(n, s, agg):
            if not s:
                if agg == n:
                    arr[n] = n**2
            
            for i in range(len(s)):
                squareSumCheck(n, s[i+1:], agg + int(s[:i+1]))
        
        for i in range(1, n+1):
            squareSumCheck(i, str(i**2), 0)

        return sum(arr)