#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
             return 0
    
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
    
        ...
        res = 0
        maxL = [0] * len(height)
        maxR = [0] * len(height)

        for i in range(0, len(height) - 1):
            if i == 0:
                maxL[i] = height[i]
                maxR[len(height) - 1 - i] = height[len(height) - 1]
            else:
                maxL[i] = max(height[i], maxL[i - 1])           
                maxR[len(height) - 1 - i] = max(height[len(height) - 1 - i], maxR[len(height) - 1 + 1 - i])
                
        for j in range(1, len(height) - 1):
            res += (min(maxL[j], maxR[j]) - height[j])       

        return res
        ... 
     
# @lc code=end

