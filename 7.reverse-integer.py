#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        upper = 2 ** 31 - 1
        lower = -upper - 1
        input_str = str(x)
        append_minus = False
        if input_str[0] == "-":
            append_minus = True
            input_str = input_str[1::]

        reversed_input = input_str[::-1]
        result = int(reversed_input)

        if append_minus:
            result = result * (-1)
        if result > upper or result < lower:
            return 0
        return result


# @lc code=end
