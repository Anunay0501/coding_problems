from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        xor_dic = defaultdict(int)
        curr_xor = 0
        xor_dic[0] += 1
        ans = 0
        
        for num in nums:
            curr_xor ^= num
            
            if curr_xor in xor_dic:
                ans += xor_dic[curr_xor]
            xor_dic[curr_xor] += 1
        
        return ans
