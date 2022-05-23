x = 0 
y = 0 

def init(a, b):  # метод, который отвечает за 
  global x       # инциализацию x и y 
  global y
  x = a
  y = b

# init(22, 7)

# print(x)
# print(y)

def do_it():       # метод сложения этих чисел 
  return x + y 