from cmath import inf


N, M = map(int, input().split())
A = list(map(int, input().split()))
Asum = [0]
for i in range(1, N):
    Asum.append(Asum[i - 1] + A[i - 1])

B = 0
for i in range(M):
    B += (i + 1)*A[i]

maxSum = B
for i in range(1, N - M + 1):
    nextB = B + M * A[i + M - 1] - (Asum[M + i - 1] - Asum[i - 1])
    maxSum = max(maxSum, nextB)
    B = nextB

print(maxSum)