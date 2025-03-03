# Benjamin Kellman
# 1/27/25

times = int(input())
decimal_count = 1
for i in range(times):
    x, y, z = input().split()
    x = int(x)
    z = int(z)
    ans = ""
    if (y=="+"):
        ans += (format(x+z, ".1f"))
        ans += " "
        ans += (format(z+x, ".1f"))
    elif(y=="-"):
        ans += (format(x-z, ".1f"))
        ans += " "
        ans += (format(z-x, ".1f"))
    elif(y=="/"):
        ans += format(int((x/z) * (10 ** decimal_count) + 0.5)/( 10 ** decimal_count), ".1f")
        ans += " "
        ans += format(int((z/x) * (10 ** decimal_count) + 0.5)/( 10 ** decimal_count), ".1f")
    else:
        ans += (format(z*x, ".1f"))
        ans += " "
        ans += (format(z*x, ".1f"))

    print(ans)