#first direct the user to type in the weight and height
# then using the bmi formula
# using if or elif branches to tell which case people are in
# to make output at each branch
wt=input("weight:")
ht=input("height:")
bmi=wt/(ht*ht)          #the formula for bmi
print("BMI:",bmi)      
if bmi<18.5:            #less than 18.5
    print("Underweight")
elif bmi>=18.5 and bmi<30:  #the second situation
    print("Normal weight")
elif bmi>=30:
    print("Obese")    #the third situation




