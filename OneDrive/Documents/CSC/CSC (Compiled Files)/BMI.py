class BMI:
    def __init__(self, height1, weight1):
        self.height = height1 
        self.weight = weight1 

    def convert(self):
        self.weight = self.weight/2.20462262 #converting weight (pounds to kilograms)
        self.height = (self.height*2.54)/100 #converting height (inches to meters) 


    def getbmi(self):
        self.bmi=self.weight/(self.height**2)
        return round(self.bmi,1)


        if self.bmi < 18.5:
            self.bmi_class = "underweight"
            print(', You are underweight')
        elif self.bmi >= 18.5 and self.bmi < 25:
            self.bmi_class =  "normal"
            print(', You are normal')
        elif self.bmi >= 25 and self.bmi < 30:
            self.bmi_class =  "overweight"
            print(', You are an overweight')
        elif self.bmi >30:
            self.bmi_class =  "obese"
            print(', You are an obese')
        else:
            self.bmi_classification = "An error occured."
            print('An error occured.')
            
            
            
    def length(self):
        try:
            if len (self.height)>=4 or len(self.weight)>=3:
                raise Exception
            else:
                self.weight = self.weight/2.20462
                self.height = (self.height*2.54)/100
        except Exception:
            return "-"

    def try_e(self):
        try:
            self.bmi=round(self.weight/(self.height**2),1)
            if self.height <=0 or self.weight<=0:
                raise Exception
            elif type(self.height) == str or type(self.weight) == str:
                raise Exception
        except Exception:
            return "-"
            
