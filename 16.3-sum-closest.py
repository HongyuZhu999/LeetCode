#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        tsum = nums[0] + nums[1] + nums[2]
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue 
            p = i + 1
            q = len(nums) - 1
            while p < q:
                threesum = nums[p] + nums[q] + a
                print(threesum)
                if target > threesum:
                        p += 1
                elif target < threesum:
                        q -= 1
                else:
                    return threesum
                if abs(threesum - target) < abs(tsum - target):
                    tsum = threesum
        return tsum     
'''
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1           
        return result
    # by Google
'''

# @lc code=end

