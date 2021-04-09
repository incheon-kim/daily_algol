"""
11724 연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""

import sys
input = sys.stdin.readline

from collections import defaultdict, deque
N, M = map(int, input().split())
graph = defaultdict(list)
visited = [False] * (N + 1)
for _ in range(M):
    e, v = map(int, input().split())
    graph[e].append(v)
    graph[v].append(e)

dq = deque()
answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        dq.append(i)
        while dq:
            e = dq.popleft()
            visited[e] = True
            for v in graph[e]:
                if not visited[v]:
                    dq.append(v)
                    visited[v] = True
        answer += 1
        dq.clear()
    
print(answer)