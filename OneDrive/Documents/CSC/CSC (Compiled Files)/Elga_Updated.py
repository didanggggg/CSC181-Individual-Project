#Renalyn Elga
#BMI Updated

class BMI:
    
    
    def __init__(self, height1, weight1):
        self.height = height1
        self.weight = weight1
        
       
    def convert(self):
        self.wf = self.weight/2.20462262
        #converting height (inches to meters) 
        self.hf = (self.height*2.54)/100
        #converting height (inches to meters) 
     
        #calculating BMI
    def getbmi(self):
        self.bmi = round(self.wf/(self.hf **2), 1)
        return(self.bmi)

        if self.bmi <= 18.5:
            self.bmi_class = "underweight"
            print(', You are underweight.')
        elif self.bmi > 18.5 and self.bmi < 25:
            self.bmi_class = "normal"
            print(', You are normal.')
        elif self.bmi > 25 and self.bmi < 30:
            self.bmi_class = "overweight"
            print(', You are an overweight.')
        elif self.bmi > 30:
            self.bmi_class = "obese"
            print(', You are an obese.')
        else:
            self.bmi_class = "An error occured"
            print(', An error occured.')
