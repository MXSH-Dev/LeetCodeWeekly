#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits.reverse()

        # print(digits)

        digits[0] += 1

        carry = False

        for i in range(0, len(digits)):
            if carry:
                digits[i] += 1
                carry = False

            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                carry = True

        if carry:
            digits.append(1)

        digits.reverse()

        return digits


# @lc code=end

s = Solution()
print(s.plusOne([9, 9, 9]))
