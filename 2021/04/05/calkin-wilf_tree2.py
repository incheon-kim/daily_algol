"""
Calkin-wlif tree 2
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXgZVRZKAtIDFASW
"""
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
results = []
for t in range(1, T+1):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    answer = 0
    while b > 1:
        count, a = divmod(a, b)
        answer += count
        a, b = b, a
    else:
        if b != 0:
            answer += a - 1
        else:
            answer = -1
    results.append(answer)
# 각각 출력하면 시간 초과 발생, 입출력을 모았다가 출력해야함.
for i in range(T):
    print("#%d %d" % (i + 1, results[i]))