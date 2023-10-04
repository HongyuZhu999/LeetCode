#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    '''
    def intToRoman(self, num: int) -> str:
        res = ""
        for key in [1000, 500, 100, 50, 10, 5 ,1]:
            res, num = self.printRoman(num, key, res)
        res = res.replace("DCCCC", "CM").replace("CCCC", "CD")    
        res = res.replace("LXXXX", "XC").replace("XXXX", "XL")
        res = res.replace("VIIII", "IX").replace("IIII", "IV")
        return res
    
    def printRoman(self, num, key, res):
        Int_to_Roman = {1:'I', 5: 'V', 10: 'X', 50: 'L',
                100: 'C', 500: 'D', 1000: 'M'}
        while num >= key:
            res += Int_to_Roman[key]
            num -= key
        return res, num
    '''

    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(values):
            res += (num//v) * numerals[i]
            num %= v
        return res   

    '''
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = "", 0
        while num:
            res += (num//values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res    
    '''



# @lc code=end

