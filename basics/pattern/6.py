def print_pattern6(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j, end='')
        print()
print_pattern6(5)