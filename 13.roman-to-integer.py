#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        s_len = len(s)
        cur_idx = 0
        output = 0
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        while cur_idx < s_len:
            if s[cur_idx] == "I":
                if cur_idx + 1 < s_len and s[cur_idx + 1] == "V":
                    output += 4
                    cur_idx += 2
                elif cur_idx + 1 < s_len and s[cur_idx + 1] == "X":
                    output += 9
                    cur_idx += 2
                else:
                    output += 1
                    cur_idx += 1
            elif s[cur_idx] == "X":
                if cur_idx + 1 < s_len and s[cur_idx + 1] == "L":
                    output += 40
                    cur_idx += 2
                elif cur_idx + 1 < s_len and s[cur_idx + 1] == "C":
                    output += 90
                    cur_idx += 2
                else:
                    output += 10
                    cur_idx += 1
            elif s[cur_idx] == "C":
                if cur_idx + 1 < s_len and s[cur_idx + 1] == "D":
                    output += 400
                    cur_idx += 2
                elif cur_idx + 1 < s_len and s[cur_idx + 1] == "M":
                    output += 900
                    cur_idx += 2
                else:
                    output += 100
                    cur_idx += 1
            else:
                output += value_map[s[cur_idx]]
                cur_idx += 1

        return output


# @lc code=end

# s = Solution()
# print(s.romanToInt("MCMXCIV"))
