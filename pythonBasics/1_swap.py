def swap(a, b):
    a, b = b, a
    return (a, b)

a, b = swap(5, 10)
print(a, b)