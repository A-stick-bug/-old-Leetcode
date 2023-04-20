def climbStairs(self, n: int) -> int:
    a = 1
    b = 1
    temp = 0

    for i in range(n):
        temp = a + b
        a = b
        b = temp

    return a
