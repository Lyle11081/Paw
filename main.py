from calculateBMI import *
from ConvertFtoC import *
#BMi or C to F
choice = input("Please select an option BMi or Convert : ")
if choice == "bmi":
    weight = float(input("Enter your weight in kg : "))
    height = float(input("Enter heightin meters : "))
    print(calculateBMI(height,weight))
elif choice == "convert":
    fahrenheitValue = input("Enter your Farenheight")
    print(FtoCconvertor(fahrenheitValue))
else:
      print("Invalid")

