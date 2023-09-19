#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p, q = 0, len(height) - 1
        res = 0

        while p < q:
            area = (q - p) * min(height[p], height[q])
            res = max(area, res)
            if height[p] < height[q]:
                p += 1
            elif height[p] >= height[q]:
                q -= 1
        return res
    
# @lc code=end

