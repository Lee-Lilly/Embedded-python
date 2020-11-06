#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Assingment 2 ToDo

# **Task 1.** How to print a list in reverse order (from last to first item) using for in loops. Operating System List
# ```
# systems = ['Windows', 'macOS', 'Linux']
# ```

# In[4]:


systems = ['Windows', 'macOS', 'Linux']
print("original list: ", systems)

res =[]
for i in range(len(systems)-1, -1, -1):
        print(systems[i])
        res.append(systems[i])
        
print("reversed list: ", res)


# ---
# **Task 2** Use reverse() method and print list before and after reverse operation.
# ```
# systems = ['Windows', 'macOS', 'Linux']
# ```

# In[5]:


systems = ['Windows', 'macOS', 'Linux']

print("original list:", systems)

systems.reverse()

print("reversed list:", systems)


# ---
# **Task 3.** The program takes a list and **swaps the first and last value of the list.**
# 
# 1. User must enter the number of elements in the list and store it in a variable.
# 2. User must enter the values of elements into the list.
# 3. The append function obtains each element from the user and adds the same to the end of the list as many times as the number of elements taken.
# 4. A temporary variable is used to swap the **first and last element in the list.**
# ```
# temp=list[0]
# list[0]=list[number-1]
# list[number-1]=temp
# ```
# 5. The newly formed list is printed.
# 

# In[3]:


length = int(input("Please specify the length of your input list"))
mylist = []
for i in range(length):
    mylist.append(input("Enter an element for your list"))
print(mylist)
temp = mylist[0]
mylist[0] = mylist[length -1]
mylist[length -1] = temp
print(mylist)


# ---
# **Task 4** Program to Calculate the Average of Numbers in a Given List
# 
# 1. User must first enter the number of elements which is stored in the variable number.
# 2. The value of I ranges from 0 to the number of elements and is incremented each time after the body of the loop is executed.
# 3. Then, the element that the user enters is stored in the variable elem.
# 4. list.append(elem) appends the element to the list.
# 5. Now the value of i is incremented to 2.
# 6. The new value entered by the user for the next loop iteration is now stored in elem which is appended to the list.
# 7. The loop runs till the value of i reaches number.
# 8. sum(list) gives the total sum of all the elements in the list and dividing it by the total number of elements gives the average of elements in the list.
# 9. round(avg,2) rounds the average upto 2 decimal places.
# 10. Then the average is printed after rounding.
# 

# In[4]:


length = int(input("Please specify the length of your number list"))
mylist = []
for i in range(length):
    mylist.append(float(input("Enter number for your list")))
print(mylist)
print("The average is:", round(sum(mylist)/length, 2))


# ---
# **Task 5** 4-Calculator program using Python
# 
# Create a simple calculator which can perform basic arithmetic operations like addition, subtraction, multiplication or division depending upon the user input.
# 
# ## Approach:
# User choose the desired operation. Options 1, 2, 3 and 4 are valid.
# ```
# # Take input from the user  
# select = int(input("Select operations form 1, 2, 3, 4 :")) 
#   
# number_1 = int(input("Enter first number: ")) 
# number_2 = int(input("Enter second number: ")) 
# ```
# Two numbers are taken and an if…elif…else branching is used to execute a particular section.
# ```
# if select == 1: 
#     print(number_1, "+", number_2, "=", 
#                     add(number_1, number_2)) 
# ```
# Using functions add(), subtract(), multiply() and divide() evaluate respective operations.

# In[3]:


print("Simple calculator")

def add(num_1, num_2):
    res = num_1 + num_2
    return res
def substract(num_1, num_2):
    res = num_1 - num_2
    return res
def multiply(num_1, num_2):
    res = num_1 * num_2
    return res
def divide(num_1, num_2):
    res = num_1 / num_2
    return res

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

while True:
    print("Please select operation -\n" 
        "1. Add\n"  
        "2. Subtract\n"  
        "3. Multiply\n" 
        "4. Divide\n" 
        "Then 5. Quit\n") 
    select = int(input("select from 1, 2, 3, 4, 5: "))

    if select == 1:
        res = add(number_1, number_2)
        print(number_1, "+", number_2, "=", res)
    elif select == 2:
        res = substract(number_1, number_2)
        print(number_1, "-", number_2, "=", res)
    elif select == 3:
        res = multiply(number_1, number_2)
        print(number_1, "*", number_2, "=", round(res,2))
    elif select == 4:
        res = divide(number_1, number_2)
        print(number_1, "/", number_2, "=", res)
    elif select == 5 :
        break
print("You quited")


# In[ ]:





