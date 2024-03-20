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

import math 

def paint_calc(height, width, cover) :
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print (f"You'll need {round_up_cans} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#


def prime_checker(number) :
  is_prime = True
  for i in range(2, number) :
    if number % i == 0 :
      is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

number = int(input("choose a number."))

prime_checker(number)