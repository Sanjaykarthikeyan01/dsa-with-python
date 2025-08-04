def print_pattern17(n):
    for i in range(n):
        for left_spaces in range(n-i-1):
            print(' ', end='')
        for alphabet in range(2*i+1):
            print(chr(65 + alphabet), end='')
        for right_spaces in range(n-i-1):
            print(' ', end='')
        print()
print_pattern17(8)