#!/usr/bin/env python
# coding: utf-8

# # Python Basics - Assingment  4
#                             

# Task 1: Create a string (name), an integer (num) and a floating point number (fnum). Assign your name to name, 25 to num and 56.78 to fnum. Print the output for all 3 variables. 

# In[1]:


#name
name = "me"

#num
num = 25

#fnum
fnum = 56.78

#print name
print(name)

#print num
print(num)

#print fnum
print(fnum)


# 
# Task 2: Use the capitalize() method to convert the first character of a string to uppercase letter. 

# In[2]:


mystring = "this is getting interesting."

#use capitalize method
mycapital_string = mystring.capitalize()

#print the capitalized string
print(mycapital_string)


# Task 3: The find() method returns the index of first occurence of the substring if it is found and if it does not find it returns -1. Use find() method to complete the code below. 

# In[3]:


text = "Python is an easy to learn language"

#find learn
result = text.find('learn')

#print result  
print("The word 'learn' is found at index:", result)



# Task 4: It is possible to assign the same value to multiple variables at once in Python. Complete the code below. 

# In[4]:


# create 3 variables a,b & c & 
# assign 1 as value to all variables in the same statement
a = b = c = 1  

#print a
print (a)

#print b
print (b)

#print c
print (c)


# Task 5: Complete tasks as in the comment below 

# In[19]:


a = "I like python"

# use the len method to print the length of the string
print(len(a)) 

# print the first character of the string
print(a[0]) 

# print the string in uppercase letters 
print(a.upper())

newtext = "%d Niin %s vastaa, %s sinne huudetaan"
# it should print 1 Niin metsä vastaa, kuin sinne huudetaan
first = 1
second = 'metsä'
third = 'kuin'
# print the newtext 

print(newtext % (first, second, third)) 


# Task 6: Create a list named mylist and include 5 different data items. (4 points)

# In[28]:


# it should contain 5 different data items
mylist =  ['Windows', True, 10, {'apple': 'mac', 'google': 'android'}, 6.6 ]

# print the entire list
print(mylist) 

# print only the second element
print(mylist[1])
print(type(mylist[1]))

# use append to add one more item to your list 
mylist.append(set({'VR','Unity','IMAX'}))

# print the entire list
print(mylist)


# Task 7: Tuple (3 points)

# In[32]:


courses = ("Introduction to IoT & Cloud", "Python Basics for IoT", "Python Project")
#use len method to print the number of items(courses) in the tuple courses.
print(len(courses)) 

# print all items in the tuple courses
for item in courses:
    print(item) 

#print the third item in the tuple
print("The third item is: ", courses[2]) 


# Task 8: Dictionary (5 points)

# In[36]:


# create a dictionary with the key as course, time and ects
# values as Python Basics, Autumn, 5
test = {'course': 'Python Basics', 'time': 'Autumn', 'ects': 5}

# use get method to print the value of the course
print(test.get('course')) 

# change the course value to Python Basics for IoT
test['course'] = 'Python Basics for IoT'  

# add the key/value pair as year:2020 to the test dictionary
test['year'] = 2020

#print the entire dictionary
print(test) 

#use pop method to remove time form the dictionary
test.pop('time')
print(test)


