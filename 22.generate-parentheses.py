#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add "(" when keyopen < n
        # only add ")" when keyclose < kenopen
        # valid if keyopen == keyclose == n
        stack = []
        res = []
        
        def backtrack(keyo, keyc):
            if keyc == keyo == n:
                # print(stack)
                res.append("".join(stack))
                return
            
            if keyo < n:
                stack.append("(")
                backtrack(keyo + 1, keyc)
                stack.pop()

            if keyc < keyo:
                stack.append(")")
                backtrack(keyo, keyc + 1)
                stack.pop()
        
        backtrack(0,0)
        return res
    
'''
def generateParenthesis(self, n: int) -> List[str]:    
        res = []
        def backtrack(open_n, closed_n, path):
            
            if open_n == closed_n == n:
                res.append(path)
                return

            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
                
        backtrack(0, 0, "")
        return res

notes:
if you are confused with the global stack and the parameters passed to the function. Here is the thing. 
the global stack has only one instance throughout the program execution, 
even inside recursion its using the same instance. whereas in parameter passing, 
param is duplicated for each recursive call. 
Hence there will be a unique param state for each level of recursion. 
Hence content of param will depend on what level of recursion its on.

if you make a fucntion call inside a function's paranthesis then the function is going to hold that state, 
here we do not need backtracking solution as the function 1 adds the open brackets 
and the closed bracket condition does not let the recursive function to run if the rule does not imply.
'''

# @lc code=end

