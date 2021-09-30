#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # if x is divisible by 10, then it will not be palindrome
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        x_str = str(x)
        result = int(x_str[::-1])
        if result != x:
            return False
        return True


# @lc code=end

# s = Solution()
# print(s.isPalindrome(0))
