import math

def factorial(firstnum):
    if firstnum  == 0:
        return 1
    else:
        return firstnum * factorial(firstnum - 1)

def number_base(firstnum, secondnum):
    if b == 'bb2':
        return f"{firstnum:b}" 
    elif b == '0o8':
        return f"{firstnum:o}"
    elif b ==' Xx16':
        return f"{firstnum:x}"
    else:
        return "Invalid Base code"


def operations(firstnum, secondnum, operator):
    if operator == 'sin':
        return math.sin(firstnum)

    elif operator == 'cos':
        return math.cos(firstnum)

    elif operator == 'tan':
        return math.tan(firstnum)

    elif operator == 'sin-1':
        if -1 <= firstnum <= 1:
            return math.asin(firstnum)
        else:
            return "Invalid input for arcsin"

    elif operator == 'cos-1':
        if -1 <= firstnum <= 1:
            return math.acos(firstnum)
        else:
            return "Invalid input for arcos"

    elif operator == 'tan-1':
        return math.atan(firstnum)

    elif operator == '+':
        return firstnum + secondnum

    elif operator == '-':
        return firstnum - secondnum

    elif operator == '*':
        return firstnum * secondnum

    elif operator == '/':
        if secondnum != 0:
            return firstnum / secondnum
        else:
            return "Cannot divide by zero"

    elif operator == 'log':
        if firstnum > 0 and secondnum > 0:
            return math.log(firstnum, secondnum)
        else:
            return "Logarithm inputs must be greater than zero"
    else:
        return "Invalid operator"
