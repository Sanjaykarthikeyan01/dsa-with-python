#number, space , number 
def print_pattern12(n):
    for i in range(1,n+1):
        for left_no in range(1,i+1):
            print(left_no, end='')

        for spaces in range(2*(n-i)):
            print(' ', end='')

        for right_no in range(i,0,-1):
            print(right_no, end='')
        print()  
print_pattern12(4)  