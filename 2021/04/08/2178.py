"""
2178 미로 탐색
https://www.acmicpc.net/problem/2178
"""

from sys import stdin
input = stdin.readline

from collections import deque
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dq = deque([(0, 0, 1)])

while dq:
    y, x, moves = dq.popleft()
    visited[y][x] = True
    if (y, x) == (N - 1, M - 1):
        print(moves)
        break
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < N and 0 <= nx < M):
            continue
        if board[ny][nx] == 1 and not visited[ny][nx]:
            dq.append((ny, nx, moves + 1))
            visited[ny][nx] = True