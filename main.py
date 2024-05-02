# def format_name(f_name, l_name):
#   """Take a first and last name and format it to return the title case version of the name."""
#   if f_name == "" or l_name == "" :
#     return "You didn't provide vaild inputs."

#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"


# print(format_name(input("What is your first name?"), input("What is your last name?")))

# format_name()  #""" """ 는 메모같은거임 독스트링

# #-----------------------


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# # TODO: Add more code here 👇
# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if month == 2 and is_leap(year) :
#     return 29
#   else:
#     return month_days[month - 1]
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)


#-------------------------계산기

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def mutiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : mutiply,
  "/" : divide,
}

num1 = input("frist number: ")
num2 = input("second number: ")
for  symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation form the line above: ")

answer1 = operations[operation_symbol](int(num1),int(num2))

print(f"{num1} {operation_symbol} {num2} = {answer1}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("next number?: "))
answer2 = operations[operation_symbol](int(answer1),int(num3))

print(f"{answer1} {operation_symbol} {num3} = {answer2}")