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
  # fix code
  print("Guess the number (1-10):")


def multiplication_table():
  """
    Using a while/for loops, implement a multiplication table.
  """
  # fix code
  print("multiplication_table for {number}")


def basic_calculator():
    def suma(num1, num2):
        return num1 + num2

    def resta(num1, num2):
        return num1 - num2

    def multiplicacion(num1, num2):
        return num1 * num2

    def division(num1, num2):
        return num1 / num2

    print("Por favor, elige una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingresa una opción (1/2/3/4): ")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        print(num1, "+", num2, "=", suma(num1, num2))
    elif opcion == '2':
        print(num1, "-", num2, "=", resta(num1, num2))
    elif opcion == '3':
        print(num1, "*", num2, "=", multiplicacion(num1, num2))
    elif opcion == '4':
        if num2 == 0:
            print("No se puede dividir por cero.")
        else:
            print(num1, "/", num2, "=", division(num1, num2))
    else:
        print("Opción inválida")


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