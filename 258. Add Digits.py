def addDigits(num):
    while num > 9:
        digit_total = 0
        temp = num
        # find sum of digits
        while temp > 0:
            digit_total += temp % 10
            temp //= 10
        num = digit_total
    return num


print(addDigits(38))
