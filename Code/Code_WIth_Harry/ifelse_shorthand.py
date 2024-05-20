import Day45
Day45.data()
age=int(input("Enter the age : "))
print("Eligible") if age>18 else print("Not Eligible")

print("Driving is ligal for heavy vehical also") if age>18 else print("Driving is Ligal only for scooter") if age>16 else print("Driving Illigal")
