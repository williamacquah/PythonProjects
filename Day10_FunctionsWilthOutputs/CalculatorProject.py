from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
to_continue = True
while True:
    first_num = float(input("What is the first number?: "))
    print("+\n-\n*\n/\n")
    math_operator = input("Pick an operation: ")
    second_num = float(input("What is the second number?: "))
    result = calc_dict[math_operator](first_num, second_num)
    print(f"{first_num} {math_operator} {second_num} = {result}")
    continue_wish = input(f"Type 'y' to continue calculating {result}, or type 'n' to start a new calculation:").lower()
    while continue_wish == "y":
        first_num = result
        print("+\n-\n*\n/\n")
        math_operator = input("Pick an operation: ")
        next_num = float(input("What is the next number?: "))
        result = calc_dict[math_operator](first_num, next_num)
        print(f"{first_num} {math_operator} {next_num} = {result}")
        continue_wish = input(f"Type 'y' to continue calculating {result}, or type 'n' to start a new calculation:").lower()





