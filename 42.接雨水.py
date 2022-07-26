#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1
        while i < len(height) - 1 and height[i] <= height[i + 1]:
            i += 1
        while j > 0 and height[j] <= height[j - 1]:
            j -= 1

        while i < j:
            if height[i] < height[j]:
                pre = i
                i += 1
                while i < j and not (height[i] >= height[i - 1] and height[i] > height[i + 1] and height[i] > height[pre]):
                    res -= min(height[i], height[pre])
                    i += 1
                res += (i - pre - 1) * min(height[pre], height[i])
            else:
                post = j
                j -= 1
                while i < j and not (height[j] > height[j - 1] and height[j] >= height[j + 1] and height[j] > height[post]):
                    res -= min(height[j], height[post])
                    j -= 1
                res += (post - j - 1) * min(height[j], height[post])
        return res

# @lc code=end
if __name__ == '__main__':
    test_cases = [
        [9,6,8,8,5,6,3],
        [5,2,1,2,1,5],
        [5,4,1,2],
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
        [2],
    ]
    for test_case in test_cases:
        print(test_case)
        res = Solution().trap(test_case)
        print(res)
