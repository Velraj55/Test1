ReadText = open(r"C:\Users\Velraj arichandran\PycharmProjects\Giraffe\employees.txt", "r")
ReadText1 = open(r"C:\Users\Velraj arichandran\PycharmProjects\Giraffe\employeesWrite.txt", "w")
ReadText2 = open(r"C:\Users\Velraj arichandran\PycharmProjects\Giraffe\employeesappend.txt", "a")
#ReadText = open("C:\Users\employees.txt", "r")

print (ReadText.readable())
print(ReadText1.writable())
print (ReadText2.writable())

#append
#if result:
 #   for employee in (ReadText.readlines()):
  #      print (employee)

#append
if (ReadText2.writable()):
    ReadText2.write("\nVelraj, Arichandran")

if (ReadText1.writable()):
    ReadText1.write("\nVelraj, Arichandran")

ReadText.close()
ReadText1.close()
ReadText2.close()
