# 2. Write a program to find the sum of two numbers.
try:
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")
    if "." in first_number or "." in second_number:
        print("The sum of ",first_number,"and",second_number,"is",float(first_number)+float(second_number))
    else:
        print("The sum of ",first_number,"and",second_number,"is",int(first_number)+int(second_number))
except ValueError:
    print("Invalid Input!")
