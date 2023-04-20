def nth_fibonacci(n):
    a, b, temp = 0, 1, 0
    for i in range(n):
        temp = a + b
        a = b
        b = temp

    return a


print(nth_fibonacci(8))