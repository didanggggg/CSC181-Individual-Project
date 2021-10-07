#Renalyn V. Elga BS Statistics III
#BMI Change Specs


class BMI:
    print("BMI Calculator\n")
    
    #input age
    age = int(input("Enter your age: "))
    #input sex (M/F)
    sex = input("Enter your sex(Male or Female): ")
    #input height in inches
    height = float(input("Enter height in inches (inch): "))
    #input weight in pounds
    weight = float(input("Enter weight in pounds (lbs): "))
    
    
    height1 =  height * 0.0254 #converting height (inches to meters) 
    weight1 = weight * 0.454 #converting weight (pounds to kilograms)

    #calculating BMI
    def BMI(height1,weight1):
        bmi = round(weight1/ (height1**2), 1)
        return bmi

    
    bmi = BMI (height1,weight1)
    print("Your BMI result is:", format(bmi))


    bmi_class = ''
    if bmi <= 18.5:
        print('You are underweight.')
        bmi_class = 'You are underweight'
    elif bmi > 18.5 and bmi < 25:
        print('You are normal.')
        bmi_class = 'You are normal'
    elif bmi >25 and bmi <30:
        print('You are an overweight.')
        bmi_class = 'You are an overweight'
    elif bmi > 30:
        print ('You are an obese.')
        bmi_class = 'You are an obese'
    else:
        print('An error occurred.')
        bmi_class = 'An error occured.'


    f=open('BMIData.txt','a')
    f.write(str(age)+ ',' +sex+ ',' +str(weight)+ ',' +str(height)+ ',' +str(bmi)+ ',' +bmi_class+'\n')
    f.close()

    f=open('BMIData.txt')
    line = 0
    while True:
        con=f.readline()
        if len(con)>0:
            print("\nAge, Sex, Weight, Height, BMI, BMI class\n",con)
        else:
            break
    

#END
        
