try:
    result = 10/0
    number = int(input("Enter a Number : "))
    print("Number is :" +str(number))

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid input entered: Enter only numbers")
