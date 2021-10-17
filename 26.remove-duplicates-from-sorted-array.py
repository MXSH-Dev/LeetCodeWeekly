#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        slow_p = 0
        fast_p = 1
        k = 1
        while fast_p < len(nums):
            if nums[fast_p] == nums[slow_p]:
                fast_p += 1
            else:
                slow_p += 1
                nums[slow_p] = nums[fast_p]
                fast_p += 1
                k += 1
        return k


# @lc code=end
