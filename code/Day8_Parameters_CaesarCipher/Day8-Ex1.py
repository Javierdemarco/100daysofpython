# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nicer today?")
#
# greet()

# Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print("Isn't the weather nicer today?")
#
# greet_with_name("Javier")

# Functions with more than 1 input
def gree_with(name, location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What is it like in {location}")

# gree_with("Javier", "Spain")
gree_with(location="Spain", name="Javier")
