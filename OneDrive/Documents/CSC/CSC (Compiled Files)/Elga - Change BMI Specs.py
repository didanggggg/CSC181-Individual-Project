#Elga, Renalyn V.
#Computing BMI (Lab Activity)

class BMI:
    print("BMI Calculator\n")

    
    #entering values of height in inches and weight in pounds
    height = float(input("Enter height in inches (inch): "))
    weight = float(input("Enter weight in pounds (lbs): "))

    
    def BMI(height1, weight1):
        bmi = round(weight1/(height1**2), 1)
        return bmi
    
    height1 =  height * 0.0254 #converting height (inches to meters) 
    weight1 = weight * 0.454 #converting weight (pounds to kilograms)

#Enter age and sex
    age = str(input("Enter your age: "))
    sex = str(input("Enter your sex: "))
    
    #calculating BMI
    bmi = BMI (height1,weight1)

    if bmi <= 18.5:
        print("You are underweight.")
    elif bmi > 18.5 and bmi < 25:
        print("You are normal.")        
    elif bmi > 25 and bmi < 30:
        print("You are overweight.")
    elif bmi > 30:
        print("You are an obese.")

    else:
            print("An error occured.")

    print("Your BMI result is:", format(bmi))


#change int float to string
str_weight = str(weight.in_kg())
str_height = str(height.in_m())
str_bmi = str(bmi)

f = open("BMI.py","a")
f.write(age)
f.write(",")
f.write(sex)
f.write(",")
f.write(str_height)
f.write(",")
f.write(str_weight)
f.write(",")
f.write(str_bmi)
f.write(",")
f.write(bmi_class)

f.close()

f = open("BMI.py","r")
print(f.read())

