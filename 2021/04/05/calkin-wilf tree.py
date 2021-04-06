"""
SW Expert Academy
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXgZSOn6ApIDFASW&categoryId=AXgZSOn6ApIDFASW&categoryType=CODE
"""
"""
test input

15
L
R
LL
LR
RL
RR
LLL
LRL
LRR
RLR
RRL
LLRLLRLRLLRRRRLRLRLLRLLRLRLLRR
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLLLRLLLLLLLLLLLLLLLLLLL
RRRRRRRRRRRRRRRRRRRRRRRRRRLRRR

"""
T = int(input())
for t in range(1, T+1):
    a, b = 1, 1
    for direction in input():
        if direction == "L":
            b = a + b
        elif direction == "R":
            a = a + b
    print("#", end="")
    print(t, a, b)