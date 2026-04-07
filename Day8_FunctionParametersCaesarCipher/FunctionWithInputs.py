def greet():
    print("Hello.")
    print("How are you?")
    print("Have a nice day!")

greet()

#Functions with 1 input
def greet_with_name(name):
    print(f"Hello {name}.")
    print(f"How are you {name}?")
    print("Have a nice day!")

greet_with_name("William")

#Functions with more than 1 input
def greet_with_name2(name = "Lee", location = "Hamburg"):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

greet_with_name2("Lee", "Hamburg")
