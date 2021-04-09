"""
4963 섬의 개수
https://www.acmicpc.net/problem/4963
"""

import sys
input = sys.stdin.readline

from collections import deque

directions = [(1,0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1)]
answer = []
while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    board = []
    count = 0
    for y in range(h):
        board.append(list(map(int, input().split())))
    def bfs(y, x):
        dq = deque([(y,x)])
        while dq:
            cur_y, cur_x = dq.popleft()
            board[cur_y][cur_x] = 0
            for dy, dx in directions:
                ny, nx = cur_y + dy , cur_x + dx
                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if board[ny][nx] == 1:
                    dq.append((ny, nx))
                    board[ny][nx] = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1:
                bfs(y,x)
                count += 1
    answer.append(count)
for count in answer:
    print(count)