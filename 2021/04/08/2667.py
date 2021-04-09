"""
2667 단지번호 붙이기
https://www.acmicpc.net/problem/2667
"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
board = []
complex, house = 1 , []
for _ in range(N):
    board.append([0 if x == "0" else -1 for x in input()])

def bfs(y, x):
    global complex, board
    dq = deque([(y,x)])
    count = 0
    while dq:
        now_y, now_x = dq.popleft()
        board[now_y][now_x] = complex
        count += 1
        for dy, dx in directions:
            ny, nx = now_y + dy, now_x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if board[ny][nx] != -1:
                continue
            board[ny][nx] = complex
            dq.append((ny ,nx))
    complex += 1
    return count

for y in range(N):
    for x in range(N):
        if board[y][x] == -1:
            house.append(bfs(y, x))

print(complex - 1)
for count in sorted(house):
    print(count)