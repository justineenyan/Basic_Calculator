#!usr/bin/python3
from arith import operations, factorial, number_base

print('''
operators can be +, -, *, /, sin,cos,tan,sin-1,cos-1,tan-1, and etc
number base: 0o2 -> binary, 0o8-> octal, Xx16-> hexadecimal
'''
)

firstnum = float(input("Enter first Number: "))
operator = input("Enter operator for the computation: ")

if operator == 'factorial':
    result = factorial(int(firstnum))
else:
    secondnum = float(input("Enter second Number: "))

if operator in ['sin', 'cos', 'tan', 'sin-1', 'cos-1', 'tan-1', '+', '-', '*', '/', 'log']:
    result = operations(firstnum, secondnum, operator)
else:
    result = number_base(int(firstnum), operator)

print("The result: ", result)
