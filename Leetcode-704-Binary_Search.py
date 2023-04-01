from bisect import bisect
from typing import List


# My own Binary serach algo

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]>=target:
                r=m
            else:
                l=m+1
        return l if nums[l]==target else -1
    
    
# Using bisect module

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind=bisect.bisect_left(nums,target)
        return ind if ind<len(nums) and nums[ind]==target else -1