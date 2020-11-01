def print_odd(start, end):
    i = 0
    while i < end:
        if i % 2 != 0:
            print(i, end=', ')
        i += 1


print_odd(0, 10)
print_odd(-10, 0)
