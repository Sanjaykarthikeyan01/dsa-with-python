# space, star, sapce
# n-i-1,2*i+1, n-i-1
def print_pattern7(n):
    for i in range(n):
        for left_space in range(n-i-1):
            print(' ', end='')
        for star in range(2*i+1):
            print('*', end='')
        for right_space in range(n-i-1):
            print(' ', end='')
        print()
print_pattern7(5)