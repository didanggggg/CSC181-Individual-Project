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
    



#END