def print_pattern18(n):
    for i in range(1, n + 1):
        start_Alphabet = 65 + n - i 
        for j in range(i):
            print(chr(start_Alphabet+ j), end=' ')
        print()

print_pattern18(5)
