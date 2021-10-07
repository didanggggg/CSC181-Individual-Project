import pytest
from BMI_PredCap import BMI

def test1():
    weight = 123
    height = 100
    gender = "Male"
    bmi = BMI(weight, height, gender) 
    result = bmi.pred_cap()
    print("Test 1 Predicted weight is ")
    print(result)
    print("\n")

def test2():
    weight = 100
    height = 90
    gender = "Female"
    bmi = BMI(weight, height, gender)
    result = bmi.pred_cap()
    print("Test 2 Predicted weight is: ")
    print(result)
    print("\n")

def test3():
    weight = 90
    height = 60
    gender = "Male"
    bmi = BMI(weight, height, gender)
    result = bmi.pred_cap()
    print("Test 3 Predicted weight is: ")
    print(result)
    print("\n")

def test4():
    weight = 70
    height = 87
    gender = "Female"
    bmi = BMI(weight, height, gender)
    result = bmi.pred_cap()
    print("Test 4 Predicted weight is: ")
    print(result)
    print("\n")

def test5():
    weight = 0
    height = 0
    gender = "Male"
    bmi = BMI(weight, height, gender)
    result = bmi.pred_cap()
    print("Test 5 Predicted weight is: ")
    print(result)
    print("\n")

def test6():
    weight = 180
    height = -1
    gender = "Male"
    bmi = BMI(weight, height, gender)
    result = bmi.pred_cap()
    print("Test 6 Predicted weight is: ")
    print(result)
    print("\n")

def test7():
    weight = 180
    height = "so"
    gender = "Female"
    bmi = BMI(weight, height, gender) 
    result = bmi.pred_cap()
    print("Test 7 Predicted weight is: ")
    print(result)
    print("\n")
    
def test8():
    weight = "a"
    height = 89
    gender = "Female"
    bmi = BMI(weight, height, gender)
    result = bmi.pred_cap()
    print("Test 8 Predicted weight is: ")
    print(result)
    print("\n")

def test9():
    
    weight = ""
    height = ""
    gender = "Male"
    bmi = BMI(weight, height, gender) 
    result = bmi.pred_cap()
    print("Test 9 Predicted weight is: ")
    print(result)
    print("\n")


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()


#End



