import time
import math
#addition function
def add(x, y):
    return x + y
# function to Subtract
def sub(x, y):
    return x - y
#function to divide
def div(x, y):
    return x / y
# function to multiply
def mul(x, y):
    return x*y
# function to find sqrt
def sqr(x):
  return math.sqrt(x)
def pwr(x, y):
    return math.pow(x, y)
# function to find greatest of two numbers
def grt(x, y):
    if x < y:
        print (y, ' is greater than ', x)
    elif x > y:
        print (x, ' is greater than ', y)
    elif x == y:
        print (y, ' is equal to  ', x)
    else:
        print ("Invalid")
# function to find factorial
def fac(x):
    return math.factorial(x)
# function to find greatest common divisor
def hcfnaive(x, y):
    return math.gcd(x, y)
# function sin, cos, tan
def cos(x):
        result = math.cos(math.radians(int(num1)))
        print("The  cos(", num1, ") is %s" % (result))

def sin(x):
        result = math.sin(math.radians(int(num1)))
        print("The  sin(", num1, ") is %s" % (result))

def tan(x):
        result = math.tan(math.radians(int(num1)))
        print("The  tan(", num1, ") is %s" % (result))
#Prints your choice to make sure you chose the right one
def name():
    if use == '1' or use == 'add':
       return 'Addition'
    if use == '2' or use == 'subtract':
        return "Subtraction"
    if use == '3' or use == 'divide':
        return "Dividision "
    if use == '4' or use == 'multiply':
        return "Multiplication"
    if use == '5' or use == 'squareroot':
        return "Squareroot"
    if use == '6' or use == 'square':
        return "Square"
    if use == '7' or use == 'power':
        return "Exponent"
    if use == '8' or use == 'comp' or use == 'compare':
        return "Compare two numbers"
    if use == '9' or use == 'factorial' or use == 'fact':
        return "Factorial"
    if use == '10' or use == 'gcd':
        return "Greatest Common divisor"
    if use == '11' or use == 'sin' or use == 'sine':
        return "Sine"
    if use == '12' or use == 'cos' or use == 'cosine':
        return "Cosine"
    if use == '13' or use == 'tan' or use == 'tangent':
        return "Tangent"
#Prints the operations list for reference
def desc():
        print("+----------------------------------------------------------------------------------------+")
        print(" Select Operation: \n 1. Add \n 2. Subtract \n 3. Divide \n 4. Multiply \n 5. Squareroot")
        print(" 6. Square \n 7. Exponential Function(power)                                            ")
        print(' 8. Compare two numbers(comp or compare) \n 9. Factorial of a number(factorial or fact) ') 
        print(' 10. Greatest common Divisor of two numbers (gcd)                                       ')
        print(" 11. Sine of a number(sin or sine) \n 12. Cosine of a number(cos or cosine              ")
        print(' 13. Tangent of a number(tan or tangent) \n 01. View the list \n 02. Simple Calculator) ')
        print(' 03. Complicated ver. of the simple calculator \n 0. Exit                               ')
        print("+-----------------------------------------------------------------------------------------+")
def diffcal():
    from collections import liops

    #reverse order of operations
    
    operations = liops([
        ("+", lambda x, y: x + y),
        ("-", lambda x, y: x - y),
        ("/", lambda x, y: x / y),
        ("*", lambda x, y: x * y),
        ("^", lambda x, y: pow(x, Y))
    ])
        
    symbols = operations.keys()

    def lex(expr):
        """
        seperates numbers from symbols, recursively nests parens
        """
        tokens = []
        while expr:
            char, *expr = expr
            #char is equal to the first charecter of the expression, expr is equal
            #to the rest of it
            if char == "#":
                #the rest of the line is a comment
                continue
            if char == "(":
                try:
                    paren, expr = lex(expr)
                    tokens.append(paren)
                    #expr is what's after the end of the paren, we'll just continue
                    #lexing after that''
                except ValueError:
                    raise Exception("parenthesis mismatch")
            elif char == ")":
                return tokens, expr
                #returns the tokens leading up to the to the paren and the rest of 
                #the expression after it
            elif char.isdigit() or char == ".":
                #number
                try:
                    if tokens[-1] in symbols:
                        tokens.append(char) #start a new num
                    elif type(tokens[-1]) is list:
                        raise Exception("parenthesis cannot be followed by numbers")
                        #no support for 5(1+1) yet
                    else:
                        tokens[-1] += char #add to last num
                except IndexError:
                    #if tokens is empty
                    tokens.append(char) #start first num
            elif char in symbols:
                tokens.append(char)
            elif char.isspace():
                pass
            else:
                raise Exception("invalid charecter: " + char)
        return tokens

    def evaluate(tokens):
        for symbol, func in operations.items():
            #try to find an operation to eval in order
            try:
                pos = tokens.index(symbol)
                #split the tokens by the operation and eval that
                leftTerm = evaluate(tokens[:pos])
                rightTerm = evaluate(tokens[pos + 1:])
                return func(leftTerm, rightTerm)
                #incidentially, return immediatly breaks all loops within the
                # function
            except ValueError:
                pass
                #index raises ValueError when it's not found
        if len(tokens) is 1:
            try:
                #it must be a number
                return float(tokens[0])
            except TypeError:
                #if it's not a number
                return evaluate(tokens[0])
        else:
            raise Exception("bad expression: " + tokens)

    def calc(expr):
        return evaluate(lex(expr))
        
    while 1:
        print(calc(input("Input? ")))
def simpcal():
     while True:
        print('\n Enter "0" or "back" to go back to the main Calculator')
        calc = input("Type calculation: ")
        if calc == 'back' or calc == '0':
            break
        elif not calc.isalpha():
            print("Answer: " + str(eval(calc)) + "\n")
        else:
            print("Invalid input, Enter a vallid expression like(1+2*(5+6)/5), or back to go back to the main calculator")
    
            
     #not so simple calculator#

   
desc()
while True:
        print("\n")
        print('To view the operations list enter: "01", "name", "functions"')
        use = input("Enter your choice(the number or the name of the function): ")
        if use.isalpha():
            use = use.lower()
        else:
            pass

            #2 number functions#
        if use in  ('1', '2', '3', '4', '7', '8', '10', 'add', 'subtract', 'divide', 'multiply', 'power', 'comp', 'compare', 'gcd'):
            print ('Your choice: ', name())
            num1 = input("Enter a number: ")
            num2 = input("Enter another number: ")
            if num1.isalpha() or num2.isalpha():
                    print("Invalid Input, Enter a number")
            else:
            
                num1 = float(num1)
                num2 = float(num2)
                if use == '1' or use == 'add':
                        print (num1, "+", num2, "=", add(num1, num2))
                elif use == '2' or use == 'subtract':
                        print (num1, '-', num2, '=', sub(num1, num2))
                elif use == '3' or use == 'divide':
                        print (num1, '/', num2, '=', div(num1, num2))
                elif use == '4' or use == 'multiply':
                        print (num1, '*', num2, '=', mul(num1, num2))
                elif use == '7' or use == 'power':
                        print (num1, ' to the power of ', num2, ' = ', pwr(num1, num2))
                elif use == '8' or use == 'comp' or use == 'compare':
                        print (grt(num1, num2))
                elif use == '10'  or use == 'gcd':
                    num1 = int(num1)
                    num2 = int(num2)
                    print ('Greatest common Divisor of ', num1, ' and ', num2, ' = ', hcfnaive(num1, num2))
                else:
                        print("")
        
        #1 number functions#
        
        elif use in ('5', '6', '9', '11', '12', '13', 'squareroot', 'square', 'factorial', 'fact', 'sin', 'sine', 'cos', 'cosine', 'tan', 'tangent'):
            print ('Your choice: ', name())
            num1 = input('Enter the number: ')
            if num1.isalpha():
                    print("Invalid Input, Enter a number")
            else:
                num1 = float(num1)
                if use == '5' or use == 'squareroot':
                        print ('Squareroot of ', num1, ' is ', sqr(num1))
                elif use == '6' or use == 'square':
                        print ('Square of ', num1, ' is ', num1*num1)
                elif use == '9' or use == 'factorial' or use == 'fact':
                        print ('Factorial of ' , num1, ' is ', fac(num1))
                elif use == '11' or use == 'sin' or use == 'sine':
                    sin(num1)
                elif use == '12'  or use == 'cos' or use == 'cosine':
                    cos(num1)
                elif use == '13'  or use == 'tan' or use == 'tangent':
                    tan(num1)
                
                else:
                    print("")

        elif use in '0' or use in 'exit':
                print("Thank you, for using the calculator...")
                time.sleep(2)
                quit()
        elif use in '01' or use in 'name' or use in 'functions':
            desc()
        elif use in '02' or use in 'simple':
            simpcal()    
        elif use in '03' or use in 'calculator':
            diffcal()
       
            
        else:
            print ("Invalid Input, choose a Number from the list, to view the list Enter '01' or 'name' or 'function's")
