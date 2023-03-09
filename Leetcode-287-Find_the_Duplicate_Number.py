class Solution:
    def findDuplicate(self, nums) -> int:
        # Same concept as cycle in linked list.
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
           
        slow = nums[0]
        
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow