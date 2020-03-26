s = 0
n = 0
l = list(range(1, 101))

while len(l) > 1:
    a, b = l.pop(0), l.pop()
    s += a + b
    n += 1

    print(f"\t current sum is: {a + b}, just added {a} and {b}")

print(f"there are {n} pairs and then total sum is: {s}")
