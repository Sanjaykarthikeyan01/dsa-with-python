# n=371 , 3^3 + 7^3 + 1^3 = 371
def armstrong_number(n):
    original_number=n
    sum=0
    while(n>0):
        last_digit=n%10
        sum+=last_digit**3
        n=n//10
    if original_number==sum:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
armstrong_number(111)