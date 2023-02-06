import collections


class Solution:
    def findAnagrams(self, s: str, p: str):
        ans = []
        if len(s) < len(p):
            return ans
        frq = collections.Counter(p)
        left = right = 0
        dic = {}

        for right, ch in enumerate(s):
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

            if right-left+1 > len(p):
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    dic.pop(s[left])
                left += 1

            if dic == frq:
                ans.append(left)


        return ans