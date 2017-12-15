def print_triangular_numbers(n):
    #x is initialized above
    x = 1
    while x <= n:
        formula = x * (x + 1) / 2
        print (x,'\t', formula)
        x += 1
    
print_triangular_numbers(5)
