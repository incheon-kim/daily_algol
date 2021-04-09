"""
7562 나이트의 이동
https://www.acmicpc.net/problem/7562
"""

import sys
input = sys.stdin.readline

from collections import deque
directions = [(1,2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

def bfs(start, end, I):
    moves = 0
    visited = [[False] * I for _ in range(I)]
    visited[start[0]][start[1]] = True
    dq = deque([start])
    while dq:
        l = len(dq)
        for _ in range(l):
            y, x = dq.popleft()
            if (y, x) == end:
                return moves
            for dy, dx in directions:
                ny, nx = dy + y, dx + x
                if not (0 <= ny < I and 0 <= nx < I):
                    continue
                if not visited[ny][nx]:
                    dq.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
        else:
            moves += 1

for _ in range(int(input().rstrip())):
    I = int(input())
    
    board = []
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    if start == end:
        print(0)
        continue
    print(bfs(start, end, I))