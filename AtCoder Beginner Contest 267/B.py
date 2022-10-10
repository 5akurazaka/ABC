S = list(map(int, input()))

if(S[0] == 1):
    print("No")
else:
    col1 = S[6]
    col2 = S[3]
    col3 = S[1] | S[7]
    col4 = S[0] | S[4]
    col5 = S[2] | S[8]
    col6 = S[5]
    col7 = S[9]
    col = [col1, col2, col3, col4, col5, col6, col7]

    left = -1
    right = -1
    for i in range(7):
        if (col[i] == 1):
           left = i
           break

    for j in range(6, -1, -1):
        if (col[j] == 1):
           right = i
           break
    if(0 in col[i + 1: j]):
        print("Yes")
    else:
        print("No")