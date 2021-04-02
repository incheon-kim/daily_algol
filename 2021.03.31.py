"""
leetcode 2021 march
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3691/
"""
from typing import List

# dfs (time out)
class Solution_DFS:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # string, history
        #q = deque([("?" * len(target), set())])
        s = [("?" * len(target), [])]
        while s:
            now, history = s.pop()
            if now == target:
                return history
            for i in range(len(target) - len(stamp) + 1):
                if not history or i not in history:
                    next = "".join((now[:i], stamp, now[i+len(stamp):]))
                    s.append((next, history + [i]))

# still greedy but reverse way
# not filling, removing character
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        history = []
        target = list(target)
        t_len, s_len = len(target), len(stamp)
        flag = True
        while flag:
            flag = False
            for i in range(t_len - s_len + 1):
                found = False
                for j in range(s_len):
                    if target[i+j] == "*":
                        continue
                    if target[i+j] != stamp[j]:
                        break
                    found = True
                else:
                    if found:
                        flag = True
                        history.append(i)
                        for j in range(s_len):
                            target[i+j] = "*"
        for c in target:
            if c != "*":
                return []
        return history[::-1]


S = Solution()
print(
    S.movesToStamp("abc", "ababc"),
    S.movesToStamp("abca", "aabcaca"),
    S.movesToStamp("qr", "qrqqqrqrqrrqrqr"),
    S.movesToStamp("aye", "eyeye")
)