def print_all_divisors(n):
    from math import sqrt
    divisors = set()
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(divisors)
print(print_all_divisors(100))  

