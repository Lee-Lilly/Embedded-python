#!/usr/bin/env python
# coding: utf-8

# # Python Basic - Assingment 6 (Class)

# ## Problem Description
# 
# The program takes the length and breadth from the user and finds the area of the rectangle using classes.

# ## Program Explanation
# 
# 1. A class called cal is created and the __init__() method is used to initialize values of that class.
# 2. Methods for adding, substracting, multiplying, dividing two numbers and returning their respective results is defined.
# 3. The menu is printed and the choice is taken from the user.
# 4. An object for the class is created with the two numbers taken from the user passed as parameters.
# 5. Using the object, the respective method is called according to the choice taken from the user.
# 6. When the choice is 0, the loop is exited.
# 7. The final result is printed.

# ## Problem Solution
# 
# 1. Create a class and using a constructor to initialize values of that class.
# 2. Create methods for adding, substracting, multiplying and dividing two numbers and returning the respective results.
# 3. Take the two numbers as inputs and create an object for the class passing the two numbers as parameters to the class.
# 4. Using the object, call the respective function depending on the choice taken from the user.
# 5. Print the final result.
# 6. Exit

# In[9]:


# Class of cal
class Cal:
    
    # constructor takes two variables
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        
    def add(self):
        return self.num_1 + self.num_2
    
    def substract(self):
        return self.num_1 - self.num_2
    
    def multiply(self):
        return self.num_1 * self.num_2
    
    def divide(self):
        return round(self.num_1 / self.num_2, 2)

# global variables
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

# Instantiate an object of Cal, passing two parameters
calculator = Cal(number_1, number_2)

while True:
    print("Please select operation -\n" 
        "1. Add\n"  
        "2. Subtract\n"  
        "3. Multiply\n" 
        "4. Divide\n" 
        "Then 0. Quit\n") 
    select = int(input("select from 1, 2, 3, 4, 0: "))
    
    if select == 1:
        res = calculator.add()
        print(number_1, "+", number_2, "=", res)
    elif select == 2:
        res = calculator.substract()
        print(number_1, "-", number_2, "=", res)
    elif select == 3:
        res = calculator.multiply()
        print(number_1, "*", number_2, "=", res)
    elif select == 4:
        res = calculator.divide()
        print(number_1, "/", number_2, "=", res)
    elif select == 0 :
        break
    else:
        print("Invalid choice!")
print("You quited")
    
    


# In[8]:


# Class of rect
class Rect:
    # constructor
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    # methods 
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return (self.length + self.breadth) * 2

# global variables
length = float(input("Enter the rectangular length: "))
breadth = float(input("Enter the rectangular breadth: "))

# Instantiate an object of Cal, passing two parameters
rectangular = Rect(length, breadth)

# Find the area and perimeter of rectangular
print("The area the rectangular: ", rectangular.area())
print("The perimeter of the rectangular is: ", rectangular.perimeter())

        

