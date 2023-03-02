# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# [x,x,y,y,z,a,a,b,b]
# [0,1,2,3,4,5,6,7,8] ----> before the single occuring element, nums[odd index]== nums[odd index-1] and nums[even ind]==nums[even ind+1].Since there is a linear order we can do a binary search.


class Solution:
    def singleNonDuplicate(self, nums) -> int:

        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l+r)//2
            if (m % 2 == 0 and nums[m] == nums[m+1]) or (m % 2 != 0 and nums[m-1] == nums[m]):
                l = m+1
            else:
                r = m
        return nums[l]
