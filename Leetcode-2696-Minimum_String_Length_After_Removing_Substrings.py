import collections


class Solution:
    def minLength(self, s: str) -> int:
        stck = collections.deque()
        for ltr in s:
            stck.append(ltr)
            while len(stck) >= 2 and (stck[-2]+stck[-1] == 'AB' or  stck[-2]+stck[-1] == 'CD'):
                stck.pop()
                stck.pop()
            
        return len(stck)