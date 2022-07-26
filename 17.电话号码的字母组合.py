#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self) -> None:
        self.digit2letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        elif n == 1:
            return self.digit2letters[digits]
        # 递归：f(n) = {digits[0]}{f(n-1)}
        else:
            return [x + y for x in self.digit2letters[digits[0]] for y in self.letterCombinations(digits[1:])]

# @lc code=end

if __name__ == '__main__':
    test_cases = [
        '23',
        '',
        '2',
        '2345'
    ]
    for test_case in test_cases:
        res = Solution().letterCombinations(test_case)
        print(test_case)
        print(res)