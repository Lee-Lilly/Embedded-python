#!/usr/bin/env python
# coding: utf-8

# # Exercise 5
# 
# **Task 1. Write a program that prompts students to provide their total points (0 -100) and check with the following conditions:**
# 
# - if total point is greater than or equal to 85 then the grade is 5
# - if total point is greater than or equal to 75 then the grade is 4
# - if total point is greater than or equal to 65 then the grade is 3
# - if total point is greater than or equal to 55 then the grade is 2
# - if total point is greater than or equal to 45 then the grade is 1
# - if total point is less than 45 then the grade is 0
# 
# (Use IF statement)
# 

# In[1]:


def grade(points):
    if points >= 85:
        grade = 5
        return grade
    if points >= 75 and points < 85:
        grade = 4
        return grade
    if points >= 65 and points < 75:
        grade = 3
        return grade
    if points >= 55 and points < 65:
        grade = 2
        return grade
    if points >= 45 and points < 55:
        grade = 1
        return grade
    if points < 45:
        grade = 0
        return grade
    
input_points = int(input("Enter you total points here: "))
print("Your grade is", grade(input_points))


# ### Example solutions Task 1.
# 
# <details><summary>CLICK ME</summary>
# <p>
# 
# ```
# #ask user to input point (Hint: use int() to cast the input to integer)
# # write conditions to check and output the grade based on point 
# 
# 
# # Example
# points = int(input("Points:"))
# if points >= 85:
#     print ("Grade: 5")
# elif points >= 75:
#     print ("Grade: 4")
# elif points >= 65:
#     print ("Grade: 3")
# elif points >= 55:
#     print ("Grade: 2")
# elif points >= 45:
#     print ("Grade: 1")
# else:
#     print ("Grade: 0")
# ```
# 
# </p>
# </details>
# 

# ---
# **Task 2. Write a  program that asks user to input a number and create the multiplication table (from 1 to 10) of a number (Use For). The output should be as below for an inputted number:**
# 
# ```
# 5 * 1 = 5
# 5 * 2 = 10
# ...
# ...
# ...
# 5 * 10 = 50
# ```

# In[2]:


def multiplication(num):
    for i in range(1, 11):
        print(num, "*", i, "=", num * i);
input_num = int(input("Enter an integer: "))
multiplication(input_num)


# ---
# **Task 3. Write a program using Numpy to generate and print 5 random number between 0 & 1.**

# In[3]:


from numpy import random
x = random.rand(5)
print(x)


# ### Example solutions Task 3.
# 
# <details><summary>CLICK ME</summary>
# <p>
# 
# ```
#  # print the 5 random numbers
# 
# # Example
# import numpy as np
# 
# for i in range(5):
#     print (np.random.random())
#     
# ```
# 
# </p>
# </details>
# 
# 

# ---
# **Task 4. Write a function to print even numbers from a list.**

# In[4]:


def evenNumber(mylist):
    evenlist =[]
    for i in mylist:
        if (int(i) % 2) == 0:
            evenlist.append(int(i))
    if len(evenlist) > 0:
        print("Even numbers: ", evenlist)
    else:
        print("no even number is found")

input_list = input("Enter numbers seaparate with comma and a space: ").split(', ')
print("input numbers: ", input_list)

evenNumber(input_list)


# ---
# **Task 5. Write a python program to write the courses list into a file called mycourses.txt and print the content of the file.**

# In[5]:


courses = ['Databases', 'NodeJS', 'DevOp', 'Basic of Python']

f = open("mycourses.txt", "w", encoding = 'utf-8') 
f.write(str(courses))
f.close()
    
f = open("mycourses.txt", "r")
print(f.read())
f.close()


# ---
# **Task 6. Append the file created in no. 5 and add the text "Here is more text".**

# In[6]:


f = open("mycourses.txt", "a")
f.write("\n Here is more text")
f.close

f = open("mycourses.txt", "r")
print(f.read())
f.close()


