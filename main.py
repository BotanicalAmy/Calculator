from art import logo
from replit import clear

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract,
    "*": multiply, 
    "/": divide,
}

def calculator():
    print(logo)
    
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
    
        #describes which math function to pass through based on the symbol entered
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again:") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()
