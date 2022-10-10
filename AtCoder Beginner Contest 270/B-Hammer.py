
pro = list(map(int, input().split()))
X = pro[0]
Y = pro[1]
Z = pro[2]

#ハンマーが必要
if((X * Y > 0) & (abs(X) > abs(Y))):
    if((Z * Y > 0) & (abs(Z) > abs(Y))):
        print(-1)
    else:
        if(X * Z > 0):
            print(abs(X))
        else:
            print(abs(Z) * 2 + abs(X))
else:
    print(abs(X))
