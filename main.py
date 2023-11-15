"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random

def guess_the_number():
  """
    Using loops, implement a guessing game.
    Guess the number (1-10):
    messages: Too low, Too high, Try again, Congratulations!
  """
<<<<<<< HEAD
  
  numeroRandom = random.randint(1, 10)
  
  
 
=======
  numeroRandom = random.randint(1, 10)

  while True:
            opcionUsuario = int(input("Guess the number (1-10): "))

            if opcionUsuario < numeroRandom:
                print("Too low. Try again.")
            elif opcionUsuario > numeroRandom:
                print("Too high. Try again.")
            else:
                print("Numero adivinado.")
                break
  
  # fix code
  print("Guess the number (1-10):")
>>>>>>> features/user1-ex1


def multiplication_table():
  """
    Using a while/for loops, implement a multiplication table.
  """
  # fix code
  print("multiplication_table for {number}")


def basic_calculator():
  """
    Using a while/for loops, implement a basic calculator.
    1. Enter the first number: 10
    2. Enter an operator (+, -, *, /): +
    3. Enter the second number: 20
    4. print 10 + 20 => Result: 30
  """
  while True:
    
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the first number: "))
    
    if operator == "+":
      result = num1 + num2
    elif operator == "-":
      result = num1 - num2
    elif operator == "*":
      result = num1 - num2
    elif operator == "*":
      result = num1 - num2
    else:
      print ("El operador no es valido") 
    print (result)
    break
   

def main():
  # input choice between 1-3 function
  # call the function
  choice = int(input(f"""
    1. Guess the number
    2. Multiplication table
    3. Basic calculator
    Enter a number (1-3): """))
  if choice == 1:
    guess_the_number()
  elif choice == 2:
    multiplication_table()
  elif choice == 3:
    basic_calculator()
  else:
    print("Invalid choice.")

main()