#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        cache = [''] * len(s)
        i = -1
        match_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            # 如果是反括号，则栈顶必须为与之对应的正括号，出栈
            if c in match_dict:
                if i >= 0 and cache[i] == match_dict[c]:
                    i -= 1
                else:
                    return False
            # 如果是正括号，则入栈
            else:
                i += 1
                cache[i] = c
        # 空栈则为完全匹配成功
        return i < 0

# @lc code=end

if __name__ == '__main__':
    test_cases = [
        '()',
        '()[]{}',
        '(]',
        '([)]',
        '{[]}',
    ]
    for test_case in test_cases:
        res = Solution().isValid(test_case)
        print(test_case)
        print(res)