"""
1707 이분 그래프
https://www.acmicpc.net/problem/1707
"""

import sys
input = sys.stdin.readline

def check(V, graph, visited):
    for now in range(1, V + 1):
        for next in graph[now]:
            if visited[now] == visited[next]:
                return False
    return True

for _ in range(int(input().rstrip())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    
    stack = []
    for i in range(1, V + 1):
        if not visited[i]:
            stack.append(i)
            visited[i] = -1
            while stack:
                now = stack.pop()
                for next in graph[now]:
                    if not visited[next]:
                        visited[next] = -visited[now]
                        stack.append(next)

    if check(V, graph, visited):
        print("YES")
    else:
        print("NO")
