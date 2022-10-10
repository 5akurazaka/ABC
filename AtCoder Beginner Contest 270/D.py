N, K = map(int, input().split())
A = list(map(int, input().split()))
B = reversed(A)

cnt = 0
minA = A[0]

DP = {0 : 0}
for n in range(1, N + 1):
    for a in A:
        if(n - a >= 0):
            if(n in DP.keys()):
                DP[n] = max(DP[n], n - DP[n - a])
            else:
                DP[n] = n - DP[n - a]


print(DP[N])