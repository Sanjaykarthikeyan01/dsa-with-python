# 02/08/2025
# 1. for the outer loop, count the number of lines(rows)
# 2. for the inner loop, focus on the columns and connect them somehow to the rows
# 3. print the pattern inside the inner for loop
# 4. observe symmetry (optional)
def print_pattern1(n):
    for i in range(n):
        for j in range (n):
            print('*', end='')
        print()
print_pattern1(5)