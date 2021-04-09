"""
7576 토마토
https://www.acmicpc.net/problem/7576
"""

import sys
input = sys.stdin.readline

from collections import deque
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]
N, M = map(int, input().rstrip().split())
board = []
ripes = deque()
total = N * M
for y in range(M):
    board.append(list(map(int, input().split())))
    for x in range(N):
        if board[y][x] == 1:
            ripes.append((y, x))
        elif board[y][x] == -1:
            total -= 1

answer = -1
while ripes:
    l = len(ripes)
    for _ in range(l):
        y, x = ripes.popleft()
        total -= 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not 0 <= ny < M or not 0 <= nx < N:
                continue
            if board[ny][nx] == 0:
                board[ny][nx] = 1
                ripes.append((ny, nx))
    answer += 1

print(-1 if total else answer)