def print_pattern8(n):
    for i in range(n):
        for left_space in range(i):
            print(' ', end='')
        for star in range(2*n-(2*i+1)):
            print('*', end='')
        for right_space in range(i):
            print(' ', end='')
        print()
print_pattern8(9)