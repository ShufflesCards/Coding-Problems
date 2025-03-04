n = int(input())

for i in range(n):
    arr = list(map(lambda x : chr(int("0x"+x,16)), input().split()))
    out = "".join(arr).lower()
    res = sum(map(lambda x: not x in ".,[]:abcdefghijklmnopqrstuvwxyz0987654321 ", out))
    print("VALID" if res == 0 else "INVALID")