class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, n = 0, len(s)
        count, ans=0, 0
        vowels = {'a','e','i','o','u'}
        
        for r, ch in enumerate(s):
            
            if ch in vowels:
                count+=1
            
            if r-l+1>k:
                if s[l] in vowels:
                    count -= 1
                l += 1
                
            ans = max(ans, count)  # putting it under condition r-l+1==k should be ideal, but it doesn't matter.
        return ans
