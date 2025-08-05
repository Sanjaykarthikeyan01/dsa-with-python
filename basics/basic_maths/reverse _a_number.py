def reverse_a_number(n):
    revere_no=0
    while(n>0):
        last_digit=n%10
        revere_no=revere_no*10+last_digit
        n=n//10
    return revere_no
print(reverse_a_number(123400))
    