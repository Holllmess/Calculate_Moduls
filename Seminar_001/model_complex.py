def calculator(a, b, c):
    x = complex(a)
    y = complex(b)
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b