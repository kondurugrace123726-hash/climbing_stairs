
n = int(input().strip())

if n == 0 or n == 1:
    print(1)
else:
    a = 1  # ways(0)
    b = 1  # ways(1)

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    print(b)