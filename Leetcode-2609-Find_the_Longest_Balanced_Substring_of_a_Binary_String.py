class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        # cz,co=count of zero and count of one respectively
        cz = co = 0
        for ch in s:
            if ch == '0':
                if co > 0:
                    cz = 1
                    co = 0
                else:
                    cz += 1
            else:
                co += 1
                if co > cz:
                    co = cz = 0
                else:
                    ans = max(ans, co*2)
        return ans
