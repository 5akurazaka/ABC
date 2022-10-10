N = int(input())
A = list(map(int, input().split(" ")))

sol = [2 for i in range(N + 1)]
for a in A:
    if(a <= N):
        sol [a] = 1

n = 0
for cnt in range(1, N + 1):
    s = sol[cnt]
    if(n + s <= N):
        n += s
    else:
        cnt -=1
        break

print(cnt)