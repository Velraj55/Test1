def FindmaxNumber(Num1,Num2,NNum3):
    if (Num1 >= Num2 ) and (Num1 >= Num3):
        print ("Num1 is greater of all")
        return Num1

    elif (Num2 >= Num1) and (Num2 >= Num3):
        print("Num2 is greater of all")
        return Num2

    elif ( Num3 >= Num1 ) and (Num3 >= Num2):
        print("Num3 is greater of all")
        return Num3

    else:
        print("all are same")
        retrun -1

Num1 = input("Enter Num1 :")
Num2 = input("Enter Num2 :")
Num3 = input("Enter Num3 :")
print(FindmaxNumber(Num1,Num2,Num3))

