#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        char_count = dict()
        sorted_strs = list(sorted(strs, key=len))
        ref_str = sorted_strs[0]

        for i in range(0, len(ref_str)):
            char_count[ref_str[i] + str(i)] = 0
            for j in range(1, len(sorted_strs)):
                if sorted_strs[j][i] == ref_str[i]:
                    char_count[ref_str[i] + str(i)] += 1

        for key in char_count:
            if char_count[key] == len(strs) - 1:
                output = output + key[0]
            else:
                break

        return output


# @lc code=end

strs = ["flower", "flow", "flight"]
s = Solution()
s.longestCommonPrefix(strs)
