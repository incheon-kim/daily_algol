"""
SWEA 4193 수영대회 결승전
https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AWKaG6_6AGQDFARV&categoryId=AWKaG6_6AGQDFARV&categoryType=CODE
"""
import sys
sys.stdin = open("input.txt", "r")
from collections import deque
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    visited = [[False for _ in range(N)] for _ in range(N)]
    answer = N ** 2
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    dq = deque([(A, B, 0)])
    while dq:
        y, x, now = dq.popleft()
        visited[y][x] = True
        if (y, x) == (C, D):
            answer = min(answer, now)
            continue
        for dy, dx in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if board[ny][nx] == 1:
                    continue
                if not visited[ny][nx]:
                    next_time = now
                    if board[ny][nx] == 2 and (now - 2) % 3 != 0:
                        while (next_time - 2) % 3 != 0:
                            next_time += 1
                    dq.append((ny, nx, next_time + 1))
                    visited[ny][nx] == True
    if answer == N ** 2:
        answer = -1
    print("#%d %d" % (t, answer))