# Well we can use inbuilt Python method
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# The first method is quite a basic method. With time complexity of O(m*n).
# So, not doing that. Look into pattern matching, came across many methods, so chose two :-
    # a) KMP algorithm
    # b) Rabin karp algorithm

# Solution using KMP algorithm


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            
            return 0

        hLen, nLen = len(haystack), len(needle)
        pi_table = [0]*nLen
        right, left = 1, 0
        
        while right < nLen:
            if needle[right] == needle[left]:
                left += 1
                pi_table[right] = left
                right += 1
            else:
                if left != 0:
                    left = pi_table[left-1]
                else:
                    right += 1

        hayInd, needInd = 0, 0
        while hayInd < hLen:
            if haystack[hayInd] == needle[needInd]:
                hayInd += 1
                needInd += 1
                if needInd == nLen:
                    return hayInd-nLen
            else:
                if needInd != 0:
                    needInd = pi_table[needInd-1]
                else:
                    hayInd += 1


        return -1
