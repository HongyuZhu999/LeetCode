#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r)//2
            time = 0
            for ba in piles:
                time += math.ceil(ba/k)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

        '''
        Time Limit Exceeded
        k = 1
        time = sum(piles[i] for i in range(len(piles)))    
        while time > h:
            time = 0
            k += 1
            for ba in piles:
                time += ba//k
                if ba%k:
                    time += 1
        return k
        '''


# @lc code=end

