import math 
def calculate():
  op = str(input('''
Please type in the operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for square
sqrt for the square root
cos for calculate the cos
sin for calculate the sin
tg for calculate the tg
ctg for calculate the ctg
hypot for calculate hypotenuse
rad for converts radians to degrees
deg for converts degrees to radians
'''))
  if op == '+':
    def addition(x,y):
      return x+y
    print(addition(float(input('Enter first number: ')),float(input('Enter second number: '))))
  elif op == '-':
    def subtraction(x,y):
      return x-y
    print(subtraction(float(input('Enter first number: ')),float(input('Enter second number: '))))
  elif op == '*':
    def multiplication(x,y):
      return x*y
    print(multiplication(float(input('Enter first number: ')),float(input('Enter second number: '))))
  elif op == '/':
    def division(x,y):
      return x/y
    print(division(float(input('Enter first number: ')),float(input('Enter second nubmer:'))))
  elif op == '**':
    def square(x,y):
      return x**y
    print(square(float(input('Enter first number: ')),float(input('Enter second nubmer: '))))
  elif op == 'sqrt':
    def sqrt(x,y):
      y=1/y
      return x**y
    print(sqrt(float(input('Enter first number: ')),float(input('Enter second nubmer: '))))
  elif op == 'cos':
    def cos(x):
      return math.cos(x)
    print(cos(float(input('Enter your number: '))))
  elif op == 'sin':
    def sin(x):
      return math.sin(x)
    print(sin(float(input('Enter your number: '))))
  elif op == 'tg':
    def tg(x):
      return math.tan(x)
    print(tg(float(input('Enter your number: '))))
  elif op == 'ctg':
    def ctg(x):
      return math.cos(x)/math.sin(x)
    print(ctg(float(input('Enter your number: '))))
  elif op == 'hypot':
    def hypot(x,y):
      return (math.sqrt(x * x + y * y))
    print(hypot(float(input('Enter first leg: ')),float(input('Enter second leg: '))))
  elif op == 'rad':
    def rad(x):
      return math.radians(x)
    print(rad(float(input('Enter your corner: '))))
  elif op == 'deg':
    def deg(x):
      return math.degrees(x)
    print(deg(float(input('Enter your corner: '))))
  else:
    print('You have not typed a valid operator, please run the program again.')
  again()
def again():
  calculate_again = str(input('''
Do you want to calculate again?
Please type Y for Yes or N for No.
''')) 
  if calculate_again == 'Y':
    calculate()
  elif calculate_again == 'N':
    print('''I'll see you.''')
  else:
    again()
    calculate()
calculate()
