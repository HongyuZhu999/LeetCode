#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue       
            p, q = i + 1, len(nums) - 1
            while p < q:
                threesum = a + nums[p] + nums[q]
                if threesum > 0:
                    q = q - 1
                elif threesum < 0:
                    p = p + 1
                else:
                    res.append([a, nums[p], nums[q]])
                    p = p + 1
                    while nums[p] == nums[p - 1] and p < q:
                        p = p + 1               
        return res 
# @lc code=end

