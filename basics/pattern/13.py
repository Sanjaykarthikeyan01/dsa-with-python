def print_pattern13(n):
    start=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(start, end=' ')
            start= start + 1
        print()        
print_pattern13(5)        