def calc(a, b, opt):
    c = 0
    
    if opt == '+':
        c = a + b
    elif opt == '-':
        c = a - b
    elif opt == '*':
        c = a * b
    elif opt == '/':
        c = a / b
    else:
        return None
    
    return c


sum = calc(10, 20, '-')

print(sum)
