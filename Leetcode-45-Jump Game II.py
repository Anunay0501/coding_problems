class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        if n <= 1: return 0
        left, right = 0, nums[0]
        jump = 1
        
        while right < n - 1:
            jump += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, nxt
        
        return jump