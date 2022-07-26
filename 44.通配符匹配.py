#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.cache = set()

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        if m == 0:
            if n == 0:
                return True
            elif p[n - 1] == '*':
                return self.isMatch(s, p[:n - 1])
            else:
                return False
        elif n == 0:
            return False
        if (m, n) in self.cache:
            return False
        self.cache.add((m, n))
        if p[n - 1] == '?' or s[m - 1] == p[n - 1]:
            return self.isMatch(s[:m - 1], p[:n - 1])
        elif p[n - 1] == '*':
            return self.isMatch(s[:m], p[:n - 1]) or self.isMatch(s[:m - 1], p[:n])
        else:
            return False

# @lc code=end

if __name__ == '__main__':
    test_cases = [
        ['aa', 'a'],
        ['aa', '*'],
        ['cb', '?a'],
        ['adceb', '*a*b'],
        ['acdcb', 'a*c?b'],
    ]
    for test_case in test_cases:
        print(test_case)
        res = Solution().isMatch(test_case[0], test_case[1])
        print(res)