class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        lastBad = lastMin = lastMax = -1
        ans = 0
        
        # We can use a sliding window with 3 pointers, one remembering where the last invalid element is,second and third remember the occurence of mink and maxk. And then we add the number of subarrays from [lastBad+1,min(lastMin,lastMax)]. Each iterating element represents the end of a potential subarray.
        for ind, num in enumerate(nums):
        
            if not minK <= num <= maxK:
                lastBad = ind
        
            elif num == minK == maxK:
                lastMin = lastMax = ind
        
            elif num == minK:
                lastMin = ind
        
            elif num == maxK:
                lastMax = ind
        
            if lastBad < min(lastMin, lastMax):
                print(ind, num, lastBad, lastMin, lastMax)
                ans += min(lastMin, lastMax)-lastBad
        
        return ans