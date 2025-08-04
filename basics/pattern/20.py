def print_pattern20(n):
    for i in range(2*n-1):
        if i < n:
            star = i + 1
        else:
            star=2*n-i-1
        for left_star in range(star):
            print('*', end='')
        for space in range(2*n - 2*star):
            print(' ', end='')
        for right_star in range(star):
            print('*', end='') 
        print()
print_pattern20(5)