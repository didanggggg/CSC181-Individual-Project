#Elga, Renalyn V.
#Adding Predictive Capability

class BMI:
    

    def __init__(self, weight, height, gender):
        self.weight = weight
        self.height = height
        self.gender = gender
    
    def convert(self):
        self.weight = self.weight/2.20462 # Converts from pounds to kgs
        self.height = (self.height*0.0254/1.00) #Converts from inches to meters
           
    def getbmi(self):
        self.bmi=self.weight/(self.height**2)
        return round(self.bmi,1)
    
    def BMI(height,weight):
        bmi = round(weight/ (height ** 2), 1)
        return bmi

    
    def try_e(self):
        try:
            self.bmi=round(self.weight/(self.height**2),1)
            if self.height <=0 or self.weight<=0:
                raise Exception
            elif type(self.height) == str or type(self.weight) == str:
                raise Exception
        except Exception:
            return "-"
    
    def length(self):
        try:
            if len (self.height)>=4 or len(self.weight)>=3:
                raise Exception
            else:
                self.weight = self.weight/2.20462
                self.height = (self.height*2.54)/100
        except Exception:
            return "-" 

    def pred_cap (self):  #pred_cap means Predictive Capability
        try:
            
            if self.gender == 'Male':
                self.gender = 1
                self.pred_weight = -244.9235 + (5.9769*self.height) + (19.3777*self.gender)
            elif self.height < 0 or self.weight < 0:
                raise Exception
            elif type(self.height) == str or type(self.weight) == str:
                raise Exception
            else:
                self.gender = 0
                self.pred_weight = -244.9235 + (5.9769*self.height) + (19.3777*self.gender)
            return round(self.pred_weight,1)
        except Exception:
            return 'Error'
    
    