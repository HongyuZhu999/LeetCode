#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {'I': 1, 'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        i = 0
        sum = 0
        while True:
            if i == (len(s) - 1):
                break
            if Roman[s[i + 1]] > Roman[s[i]]:
                sum -= Roman[s[i]]
            else:
                sum += Roman[s[i]]
            i += 1                
        sum += Roman[s[i]]
        return sum

'''
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
'''
# @lc code=end

