# Severely underweight if BMI < 16
# Underweight if BMI is between 16 and 18.5
# Normal if BMI is between 18.5 and 25
# Overweight if BMI is between 25 and 30
# Obese if BMI is more than 30

height=int(input("nhap chieu cao"))
weight=int(input("nhao can nang"))
height=height/100

bmi=weight/(height*height)
if bmi<16 :
    print("severely underweight")
elif bmi>=16 and bmi<=18.5:
    print("underweight")
elif bmi>18.5 and bmi<=25:
    print("normal")
elif bmi>25 and bmi<=30:
    print("overweight")
else :
    print("obese")
