class Solution:
    def partitionString(self, s: str) -> int:
        ans, curr = 0, set()
        for ch in s:
            if ch not in curr:
                curr.add(ch)
            else:
                ans += 1
                curr = set(ch)
        return ans+1
