#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start



class Solution:

    def __init__(self) -> None:
        self.cache = set()

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # 曾经走过的记录，未返回True，则为False
        if (m, n) in self.cache:
            return False
        self.cache.add((m, n))
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if p[j] == '.' or s[i] == p[j]:
                i -= 1
                j -= 1
            elif p[j] == '*':
                if p[j - 1] == '.' or s[i] == p[j - 1]:
                    # 动态规划，当前字符可以被-*匹配的话，可以不被-*匹配，也可以被-*匹配
                    return self.isMatch(s[:i + 1], p[:j - 1]) or self.isMatch(s[:i], p[:j + 1])
                else:
                    # 当前字符不可以被-*匹配
                    return self.isMatch(s[:i + 1], p[:j - 1])
            else:
                return False
        
        # 已被完全匹配，忽略-*
        while j >= 0 and p[j] == '*':
            j -= 2

        return i < 0 and j < 0

# @lc code=end

if __name__ == '__main__':
    test_cases = [
        ['aa', 'a'],
        ['aa', 'a*'],
        ['aa', 'a.*'],
        ['aa', 'aaa.*'],
        ['aa', 'aa.*'],
        ["ab", ".*"],
        ["aab", "c*a*b"],
    ]
    for test_case in test_cases:
        res = Solution().isMatch(test_case[0], test_case[1])
        print(test_case)
        print(res)
