#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3: return False

        dstack = deque()
        max_third= float('-inf')

        for i in range(length - 1, -1, -1):
            current_number = nums[i]

            if current_number < max_third:
                return True
            
            while dstack and dstack[0] < current_number:
                max_third = dstack.popleft()
                print(max_third)
            
            dstack.appendleft(current_number)

        return False

# @lc code=end

