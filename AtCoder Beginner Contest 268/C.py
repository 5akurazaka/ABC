N = int(input())
Hito = [i for i in range(N)]
from collections import deque
P = list(map(int, input().split()))
C = [0]*N

for i in range(N):
    #ピタリ賞
    C[(N + i - P[i]) % N] += 1
    C[(N + i - P[i] - 1) % N] += 1
    C[(N + i - P[i] + 1) % N] += 1

print(max(C))