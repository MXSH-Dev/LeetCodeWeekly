#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return [i, j]


# @lc code=end
