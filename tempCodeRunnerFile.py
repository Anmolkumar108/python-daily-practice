try:
    number1 = int(input("Enter First Number: "))
    number2 = int(input("Enter Second Number: "))
    print(number1 / number2)

except ValueError:
    print("Please Enter Number Only")
except ZeroDivisionError :
    print("Cannot divide by zero")