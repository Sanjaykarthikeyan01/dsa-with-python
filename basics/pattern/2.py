def print_pattern2(n):
    for i in range(n):
        for j in range(i):
            print('*', end='')
        print()  
print_pattern2(5)    

