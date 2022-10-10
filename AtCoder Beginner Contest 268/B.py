S = input()
T = input()

flg = True
if(len(S) <= len(T)):
    for i in range(len(S)):
        if(S[i] != T[i]):
            flg = False
            break
else:
    flg = False

if(flg):
    print("Yes")
else:
    print("No")