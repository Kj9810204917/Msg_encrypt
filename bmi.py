weight=float(input("Enter the weight:"))
Height=float(input("Enter the Height:"))
BMI=weight/Height**2
if (BMI<18.5):
    print("you are under weight ")
elif(BMI>=18.5 or BMI<25):
    print("you are normal")
elif(BMI>=25 or BMI<30):
    print("you are over weight")
elif(BMI>=30):
    print("obasity")
else:
    print("error")