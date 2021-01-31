Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your weight in Kg: "))
Height = Height/100
BMI = Weight/(Height*Height)
print("Your Body-Mass-Index is: ", BMI)
if (BMI>0):
    if(BMI<=16):
        print("You are severely underweight")
    elif(BMI<=18.5):
        print("Your are underweight")
    elif(BMI<=25):
        print("Your are Healthy")
    elif(BMI<=30):
        print("You are Overweight")
    else: print("You are Severely Overweight")
else:("Enter valid details")