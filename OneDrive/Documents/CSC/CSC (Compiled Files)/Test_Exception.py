#Renalyn V. elga
#BMITextException


import pytest
from BMI import BMI

def test1():

    # Setup

    height = 60
    weight = 60

    # Action

    temp = BMI(height,weight)
    temp.convert()
    result = temp.getbmi()
    

    # Assert

    assert result == 11.7

def test2():

    # Setup

    height = 89
    weight = 500

    # Action

    temp = BMI(height,weight)
    temp.convert()
    result = temp.getbmi()
    

    #Assert

    assert result == 44.4

def test3():

    # Setup

    height = 66
    weight = 156

    # Action

    temp = BMI(height,weight)
    temp.convert()
    result = temp.getbmi()
    

    # Assert

    assert result ==25.2

def test4():

    # Setup

    height = 59
    weight = 97

    # Result

    temp = BMI(height,weight)
    temp.convert()
    result = temp.getbmi()  

    # Assert

    assert result == 19.6

def test5():

    # Setup

    height = 79
    weight = 180

    # Action

    temp = BMI(height,weight)
    temp.convert()
    result = temp.getbmi()
    

    # Assert

    assert result == 20.3
def test6():
    
    # Setup
    
    height =0
    weight =0
    
    # Action

    temp = BMI(height,weight)
    temp.convert()
    result = temp.try_exception()

    # Assert
    
    assert result == "-"
    
def test7():
    
    # Setup
    
    height =180
    weight =-1

    # Action
    
    temp = BMI(height,weight)
    temp.convert()
    result = temp.try_exception()

    # Assert
    
    assert result == "-"
    
def test8():
    
   # Setup
    
    height =89
    weight ="a"
    
    # Action

    temp = BMI(height,weight)
    #temp.convert()
    result = temp.try_exception()

    # Assert
    
    assert result == "-"
def test9():
    
    # Setup
    
    height ="so"
    weight =180
    
    # Action

    temp = BMI(height,weight)
    #temp.convert()
    result = temp.try_exception()

    # Assert
    
    assert result == "-"
def test10():
    
    # Setup
    
    height =""
    weight =""
    
    # Action

    temp = BMI(height,weight)
    #temp.convert()
    result = temp.try_exception()

    # Assert
    
    assert result == "-"
    
def test11():
    
    # Setup
    
    height =1000000
    weight =10000
    
    # Action

    temp = BMI(height,weight)
    temp.convert()
    result = temp.length()

    # Assert
    
    assert result == "-"


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
#END
