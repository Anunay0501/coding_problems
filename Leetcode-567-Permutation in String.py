import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # All you want to do is run a sliding window in s2 of length s1 (n1). If frequency of each character in s1 and in that window matches then we return True.
        # Time complexity- O(n1+26*n2) --> O(n), Space complexity - O(2*n1) --> O(n)

        n1 = len(s1)
        frq = collections.Counter(s1)
        dic = {}

        for ind, ch in enumerate(s2):

            if ch in dic:
                dic[ch] += 1

            else:
                dic[ch] = 1

            if ind-n1 >= 0:
                dic[s2[ind-n1]] -= 1

                if dic[s2[ind-n1]] == 0:
                    dic.pop(s2[ind-n1])

            if ind+1 >= n1:

                if dic == frq:
                    return True

        return False

        # optimization possibilities - (1) creating array of 26 size and adding frequencies to those ascci of characters. But I don't think this will perform much better because you will always compare 26 spaces while in hash table you won't do that always.