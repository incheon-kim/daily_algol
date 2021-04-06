"""
leetcode 2021 april
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/
"""
# deque에 넣어서 해결했지만, slow-fast 포인터 사용해서 반으로 나누고 역참조 만들면 더 빠르게, 공간 복잡도 작게 해결가능

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        count = 0
        dq = deque()
        while head:
            dq.append(head.val)
            head = head.next
        while dq:
            left = dq.popleft()
            if not dq:
                break
            right = dq.pop()
            if left != right:
                return False
        return True

