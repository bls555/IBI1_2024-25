#don't need pseudocode
wt=input("weight:")
ht=input("height:")
bmi=wt/(ht*ht)
print("BMI:",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<30:
    print("Normal weight")
elif bmi>=30:
    print("Obese")




