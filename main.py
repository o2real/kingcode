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
def calculation():
  num1 = input("frist number: ")
  for  symbol in operations:
    print(symbol)
  should_countinue = True

  while should_countinue :
    operation_symbol = input("Pick an operation : ")
    num2 = input("next number: ")
    answer = operations[operation_symbol](float(num1),float(num2))

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calcilating with {answer}, or type 'n' to exit.: ") == "y":
      num1 = answer

    else:
      should_countinue = False
      calculation()


calculation()
