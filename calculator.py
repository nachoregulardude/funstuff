import math
import time
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
    if use == '1':
       return 'Addition'
    if use == '2':
        return "Subtraction"
    if use == '3':
        return "Dividision"
    if use == '4':
        return "Multiplication"
    if use == '5':
        return "Squareroot"
    if use == '6':
        return "Square"
    if use == '7':
        return "Exponent"
    if use == '8':
        return "Compare two numbers"
    if use == '9':
        return "Factorial"
    if use == '10':
        return "Greatest Common divisor"
    if use == '11':
        return "Sine"
    if use == '12':
        return "Cosine"
    if use == '13':
        return "Tangent"
#Prints the operations list for reference
def desc():
        if use == '01':
            print ("Select Operation: \n 1. Add \n 2. Subtract \n 3. Divide \n 4. Multiply \n 5. Squareroot \n 6. Square \n 7. Exponential Function ")
            print(' 8. Compare two numbers \n 9. Factorial of a number \n 10. Greatest common Divisor of two numbers \n 11. Sine of a number') 
            print(" 12. Cosine of a number \n 13. Tangent of a number \n 0. Exit")
        
 #not so simple calculator#

   

print ("Select Operation: \n 1. Add \n 2. Subtract \n 3. Divide \n 4. Multiply \n 5. Squareroot \n 6. Square \n 7. Exponential Function ")
print(' 8. Compare two numbers \n 9. Factorial of a number \n 10. Greatest common Divisor of two numbers \n 11. Sine of a number') 
print(" 12. Cosine of a number \n 13. Tangent of a number \n 0. Exit")
while True:
        print("\n")
        print('To view the operations list enter: "01"')
        use = input("Enter your choice: ")

            #2 number functions#
        if use in  ('1', '2', '3', '4', '7', '8', '10'):
            print ('Your choice: ', use, '.', name())
            num1 = input("Enter a number: ")
            num2 = input("Enter another number: ")
            if num1.isalpha() and num2.isalpha():
                    print("Invalid Input, Enter a number")
            else:
                num1 = float(num1)
                num2 = float(num2)
                if use == '1':
                        print (num1, "+", num2, "=", add(num1, num2))
                elif use == '2':
                      
                        print (num1, '-', num2, '=', sub(num1, num2))
                elif use == '3':
                        print (num1, '/', num2, '=', div(num1, num2))
                elif use == '4':
                        print (num1, '*', num2, '=', mul(num1, num2))
                elif use == '7':
                        print (num1, ' to the power of ', num2, ' = ', pwr(num1, num2))
                elif use == '8':
                        print (grt(num1, num2))
                elif use == '10':
                    num1 = int(num1)
                    num2 = int(num2)
                    print ('Greatest common Divisor of ', num1, ' and ', num2, ' = ', hcfnaive(num1, num2))
                else:
                        print("")
        
        #1 number functions#
        
        elif use in ('5', '6', '9', '11', '12', '13'):
            print ('Your choice: ', use,' ', name())
            num1 = input('Enter the number: ')
            if num1.isalpha() and num2.isalpha():
                    print("Invalid Input, Enter a number")
            else:
                num1 = float(num1)
                if use == '5':
                        print ('Squareroot of ', num1, ' is ', sqr(num1))
                elif use == '6':
                        print ('Square of ', num1, ' is ', num1*num1)
                elif use == '9':
                        print ('Factorial of ' , num1, ' is ', fac(num1))
                elif use == '11':
                    sin(num1)
                elif use == '12':
                    cos(num1)
                elif use == '13':
                    tan(num1)
                
                else:
                    print("")

        elif use in '0':
                print("Thank you, for using the calculator...")
                time.sleep(2)
                quit()
        elif use in '01':
            desc()
            
        else:
            print ("Invalid Input, choose a Number from the list above")
