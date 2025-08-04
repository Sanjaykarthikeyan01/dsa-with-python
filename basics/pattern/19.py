def print_pattern19(n):
    for first_half in range(n):
        for left_star in range(n-first_half):
            print('*', end='')
        for space in range(2*first_half):
            print(' ', end='')
        for right_star in range(n-first_half):
            print('*', end='')
        print()
    for second_half in range(n):
        for left_star in range(second_half+1):
            print('*', end='')
        for space in range(2*n-(2*second_half)-2):
            print(' ', end='')
        for right_star in range(second_half+1):
            print('*', end='')
        print()
print_pattern19(5)
    
        