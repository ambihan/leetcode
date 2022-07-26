#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        # 找到i使得nums[i - 1] < nums[i]，nums[i] ~ nums[n - 1]为递减序列
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        # 找出最小的且大于nums[i - 1]的数，与之调换，nums[i] ~ nums[n - 1]仍为递减序列
        if i > 0:
            j = n - 1
            while j > i and nums[j] <= nums[i - 1]:
                j -= 1
            tmp = nums[i - 1]
            nums[i - 1] = nums[j]
            nums[j] = tmp
        # 首位调换使nums[i] ~ nums[n - 1]为递增序列
        j = n - 1
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

# @lc code=end

if __name__ == '__main__':
    test_cases = [
        [1,3,2],
        [1,2,3],
        [3,2,1],
        [1,1,5],
    ]
    for test_case in test_cases:
        print(test_case)
        Solution().nextPermutation(test_case)
        print(test_case)