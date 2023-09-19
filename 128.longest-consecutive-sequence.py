#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result = 0

        for n in nums:
            length = 0
            # check if it is the strat of the sequence
            if (n - 1) not in numSet:
                while (n + length) in numSet:
                    length += 1
            result = max(length, result)
        return result
# @lc code=end

