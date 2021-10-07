#Renalyn Elga
#Automating the BMI Testing Specs

import pytest
from Elga_Updated import BMI

def test1():
    
    # Setup
    
    height = 60
    weight = 60
    
    # Action

    temp = BMI(height, weight)
    temp.convert()
    result = temp.getbmi()
    print(result)
    print('Underweight')
    
    # Assert
    
    assert result == 11.7

def test2():
    
    # Setup
    height = 89
    weight = 500
   
    #Action
    temp = BMI(height, weight)
    temp.convert()
    result = temp.getbmi()
    print(result)
    print('Obese')
    
    # Assert
    
    assert result == 44.4

def test3():
    
    # Setup
    
    height = 66
    weight = 156
    
    #Action
    
    result = temp = BMI(height, weight)
    temp.convert()
    result = temp.getbmi()
    print(result)
    print('Overweight')
    
    #Assert
    
    assert result == 25.2

def test4():
    
    # Setup
    
    height = 59
    weight = 97

    #Action
    
    temp = BMI(height, weight)
    temp.convert()
    result = temp.getbmi()
    print(result)
    print('Normal')
    
    #Assert
    
    assert result == 19.6

def test5():
    
    # Setup
    height = 79
    weight = 180
    
    #Action
    
    result = temp = BMI(height, weight)
    temp.convert()
    result = temp.getbmi()
    print(result)
    print('Normal')
    
    #Assert
    
    assert result == 20.3

test1()
test2()
test3()
test4()
test5()


#END
