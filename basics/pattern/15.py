def print_pattern14(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65 + j), end=' ')
        print() 
print_pattern14(5)  