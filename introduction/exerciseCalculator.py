# Welccalculator=Noneat greets the user and calls the calculate function.
# The calculator function presents the available operations and prompts the user's choice.
# It verifies if the chosen option is correct and performs the corresponding calculation.
# Then, it asks the user if they want to calculate again, calling the calculate function again or ending the program.

def wellcome():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('      Wellcome to the calculator')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    operation()
def operation():
    print('\nPlease, enter the operation you want: ')
    operation = int(input('(1) Addition;\n'
          '(2) Subtraction;\n'
          '(3) Division;\n'
          '(4) Multiplication;\n'
          'Enter the operation to be performed: '))
    if (operation!=1 and operation!=2 and operation!=3 and operation!=4):
        print('Operation not supported!')
        operation()
    else:
        firstNumber = float(input('Enter the first number: '))
        secondNumber = float(input('Enter the second number: '))
        result = calculator(firstNumber, secondNumber, operation)
        print('The result is: ', result)

def calculator(n1, n2, op):
    result = 0.0
    if op == 1:
        result = n1 + n2
    elif op == 2:
        result = n1 - n2
    elif op == 3:
        result = n1 / n2
    else:
        result = n1 * n2
    return result
def calculateAgain():
    return

wellcome()