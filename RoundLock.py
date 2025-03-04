decimal_count = 1
n=1.45
print(n)
print(round(1.45, 1))
print(int(n * (10 ** decimal_count) + 0.5)/( 10 ** decimal_count))

def round(n, dec): return (int(n * (10 ** dec) + 0.5)/( 10 ** dec))
