"""
13023 ABCDE
https://www.acmicpc.net/problem/13023
"""

import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * N

    def dfs(now, depth):
        visited[now] = True
        if depth == 5:
            return True
        for next in graph[now]:
            if not visited[next]:
                if dfs(next, depth + 1):
                    return True
        visited[now] = False
        return False


    for i in range(N):
        if dfs(i, 1):
            return 1
    return 0

print(solve())