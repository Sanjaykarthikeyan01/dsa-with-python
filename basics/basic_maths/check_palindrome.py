def check_palindrome(n):
    original_number=n
    reversed_number=0
    while n>0:
        last_digit=n % 10
        reversed_number=reversed_number*10+last_digit
        n=n//10
    if original_number==reversed_number:
        print("Palindrome")
    else:
        print("Not a Palindrome")
check_palindrome(12321)