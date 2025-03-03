decimal_count = 1
n=12.35

print(int(n * (10 ** decimal_count) + 0.5)/( 10 ** decimal_count))
x=int(n * (10 ** decimal_count) + 0.5)/( 10 ** decimal_count)

print(format(x, ".4f"))