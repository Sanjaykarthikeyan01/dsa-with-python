def print_pattern4(n):
    for i in range(n+1):
        for j in range(i):
            print(i, end= '')
        print()
print_pattern4(5)