def print_pattern10(n):
    for i in range(2*n-1):
       if i<n:
            star=i+1
       else:
           star=2*n-i-1
       for j in range(star):
                 print('*', end='')
       print()
print_pattern10(5)      