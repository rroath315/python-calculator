import art


#FUNCTIONS subtract, multiply, divide, and add
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def add(n1, n2):
    return n1 + n2

#add 4 functions into DICTIONARY: Keys = "+, -, *, /"
#no () for functions, don't want to trigger it, just store it
math_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calc():
    print(art.logo)

    #user making calculations with operators
    accumulate_continue = True
    first_num = float(input("Enter the first number: "))

    while accumulate_continue:
        for symbol in math_functions:
            print(symbol)
        operator = input("Enter mathematical operator: ")
        second_num = float(input("Enter the second number: "))
        result = math_functions[operator](first_num, second_num)

        print(f"{first_num} {operator} {second_num} = {result}")

        continue_calc = input(f"Type 'y' to continue calculations with {result} or 'n' to create a new calculation: ")
        if continue_calc == 'y':
            first_num = result
        else:
            accumulate_continue = False
            print("\n" * 20)
            calc()

calc()