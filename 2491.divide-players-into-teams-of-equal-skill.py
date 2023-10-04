#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#

# @lc code=start
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if (len(skill)%2) == 1 or len(skill) == 0:
            return -1
        skill.sort()      
        l, r = 0, len(skill)-1
        key_sum = skill[l] + skill[r]
        teamlist = []
        while l < r:
            sum = skill[l] + skill[r]
            if not sum == key_sum:
                return -1
            teamlist.append([skill[l],skill[r]])
            l += 1
            r -= 1
        res = 0
        for i in teamlist:
            res += i[0]*i[1]
        return res
            
# @lc code=end

