#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j, k = 0, 0, 0
        pre_max, cur_max = 0, 0
        
        while k * 2 <= m + n:
            pre_max = cur_max
            if i == m:
                cur_max = nums2[j]
                j += 1
            elif j == n:
                cur_max = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                cur_max = nums1[i]
                i += 1
            else:
                cur_max = nums2[j]
                j += 1
            k += 1

        if (m + n) % 2 == 1:
            return cur_max
        else:
            return (pre_max + cur_max) / 2

# @lc code=end

if __name__ == '__main__':

    inputs = [
        [[3], [-2,-1]],
        [[], [1]],
        [[1,2], [3,4]],
        [[0,0,0,0,0], [-1,0,0,0,0,0,1]]
    ]
    for input in inputs:
        res = Solution().findMedianSortedArrays(input[0], input[1])
        print(input)
        print(res)