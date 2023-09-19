#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+":
                stack.append(stack.pop() + stack.pop())
            elif s == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b-a))
            elif s == "*":
                stack.append(stack.pop() * stack.pop())
            elif s == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(s))
        return stack[0]
# @lc code=end

