#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, k in enumerate(nums):
            if k == target:
                return i
        return -1
# @lc code=end

