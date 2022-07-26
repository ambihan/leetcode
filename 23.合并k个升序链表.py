#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        res_head = ListNode()
        cur_node = res_head
        while True:
            k = -1
            # 找出n个链表中最小的头
            for i in range(n):
                if lists[i] and (k == -1 or lists[i].val < lists[k].val):
                    k = i
            # 如果n个链表都为空，程序结束
            if k == -1:
                return res_head.next
            # 将当前最小节点插入结果
            else:
                cur_node.next = lists[k]
                cur_node = cur_node.next
                lists[k] = lists[k].next
        


# @lc code=end

