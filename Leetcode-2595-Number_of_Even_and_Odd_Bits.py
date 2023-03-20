from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans, s = [0, 0], bin(n)[2:]
        for ind, ch in enumerate(s):
            if (len(s)-1-ind) % 2 == 0 and ch == '1':
                ans[0] += 1
            if (len(s)-1-ind) % 2 != 0 and ch == '1':
                ans[-1] += 1
        return ans
    