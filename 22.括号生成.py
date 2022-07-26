#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    # 使用动态规划解法
    def generateParenthesis(self, n: int) -> List[str]:
        res = [['']]
        for i in range(1, n + 1):
            # 初始化res[i]
            res.append([])
            for j in range(0, i): 
                # 动态规划公式：f[n] = (f[i])f[n-i-1], i = 0, 1, ..., n-1
                res[i] += [f'({x}){y}' for x in res[j] for y in res[i - 1 - j]]
        return res[n]

    # 使用深度优先搜索解法
    def generateParenthesis2(self, n: int) -> List[str]:
        res = []
        self.dfs('', n, n, res)
        return res

    # 深度优先搜索
    def dfs(self, s, m, n, res):
        # 括号用完，字符串拼装完成
        if m == 0 and n == 0:
            res.append(s)
        # 还有左括号，使用左括号加入字符串
        if m > 0:
            self.dfs(f'{s}(', m - 1, n, res)
        # 还有右括号，且剩余数量大于左括号，使用右括号加入字符串
        if n > 0 and n > m:
            self.dfs(f'{s})', m, n - 1, res)


# @lc code=end

if __name__ == '__main__':
    test_cases = [
        1,
        2,
        3,
        4,
        5,
    ]
    for test_case in test_cases:
        res = Solution().generateParenthesis2(test_case)
        print(test_case)
        print(res)