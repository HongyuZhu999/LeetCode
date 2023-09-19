#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

        '''
        l, r = nums[0], nums[len(nums)-1]
        if l <= r:
            return l
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]        
        '''

        
# @lc code=end

