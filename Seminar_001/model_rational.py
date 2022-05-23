from fractions import Fraction

def calculator(a, b, c):
  a = Fraction.from_float(a)
  b = Fraction.from_float(b)
  if c == '+': 
    return a + b 
  if c == '-':
    return a - b 
  if c == '*':
    return a * b
  if c == '/':
    return a / b