# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet() :
#   print("hello world!")
#   print("how do you do?")
#   print("Isn't the weater nice today?")


# greet()


# #

# def greet_with_name(name):
#   print(f"hello {name}!")
#   print(f"how do you do {name}?")
#   print(f"Isn't the weater nice today?")

# greet_with_name("Jioh")


#Functions with more than 1 input
def greet_with(name, location) :
  print(f"Hello {name}")
  print(f"What is it like in {location}")

# greet_with("Jioh", "Korea")

greet_with(location="Korea", name="Jioh")

#range , for 복습