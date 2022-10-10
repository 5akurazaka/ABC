S = ["" for x in range(10)]
A, B, C, D = 10, 10, 1, 10

for i in range(10):
    S[i] = input()

for i in range(10):
    if("#" in S[i]):
        A = min(A, i + 1)
        if("." in S[i]):
            for j in range(10):
                if(S[i][j] == "#"):
                    C = j + 1
                    break
            for j in range(9, -1, -1):
                if(S[i][j] == "#"):
                    D = j + 1
                    break
    if ((A < 10) & ("#" not in S[i])):
        B = min(B, i)
        break

print(A, B)
print(C, D)