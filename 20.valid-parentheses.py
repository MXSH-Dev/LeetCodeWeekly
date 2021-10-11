#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        left_count = 0
        right_count = 0

        if s[0] in [")", "}", "]"]:
            return False

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
                left_count += 1
            elif i == ")":
                right_count += 1
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
            elif i == "}":
                right_count += 1
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
            elif i == "]":
                right_count += 1
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()

        if len(stack) == 0 and left_count == right_count:
            return True
        else:
            return False


# @lc code=end
