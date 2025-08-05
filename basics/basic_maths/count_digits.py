# 7789 %10 =9 and 7789 //10 = 778.9 integer part is 778

def count_digits(n):
    count=0
    while(n>0):
        n=n//10
        count+=1
    return count
print(count_digits(7789))
