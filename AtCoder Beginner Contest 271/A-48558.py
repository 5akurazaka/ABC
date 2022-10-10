N = int(input())

first = N % 16
second = int((N - first)/16)

def toByte(N : int):
    if (N < 10):
        return  str(N)
    if (N == 10):
        return "A"
    if (N == 11):
        return "B"
    if (N == 12):
        return "C"
    if (N == 13):
        return "D"
    if (N == 14):
        return "E"
    if (N == 15):
        return "F"

print(toByte(second) + toByte(first))
