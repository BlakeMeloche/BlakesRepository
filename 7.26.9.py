def print_triangular_numbers(n):
    total = 0
    startValue = 1
    while n >=startValue:
        total += startValue
        print(startValue, "\t", total)
        startValue += 1

print_triangular_numbers(5)
