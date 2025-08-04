def print_pattern14(n):
    for i in range(n+1):
        for j in range(i):
            print(chr(64+i), end=' ')
        print() 
print_pattern14(5)  