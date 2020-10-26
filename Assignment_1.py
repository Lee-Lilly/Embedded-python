#!/usr/bin/env python
# coding: utf-8

# ---
# # Python Basics - Assignment 1 TODO

# **Task 1:** Create a string (name), an integer (num) and a floating point number (fnum). Assign your name to name, 25 to num and 56.78 to fnum. Print the output for all 3 variables.
# ```
# ###name - use your own name
# #num
# #fnum
# #print name
# #print num
# #print fnum
# ##continue to code solution cell below.
# ```

# In[2]:


name = "Lee"
num = 25
fnum = 56.78
print (name, num, fnum)


# **Task 2:** Use the capitalize() method to convert the first character of a string to uppercase letter.
# Continue to code solution cell below.
# ```
# mystring = "this is getting interesting."
# mycapital_string = #use capitalize method
# print the capitalized string
# ```

# In[6]:


mystring = "this is getting interesting."
mycapital_string = mystring.capitalize()
print (mycapital_string)


# **Task 3:** The find() method returns the index of first occurence of the substring if it is found and if it does not find it returns -1. Use find() method to complete the code below.
# ```
# text = "Python is an easy to learn language"
# result = #find learn
# print (result)
# ```

# In[8]:


text = "Python is an easy to learn language"
result = text.find('learn')
print (result)


# **Task 4:** It is possible to assign the same value to multiple variables at once in Python. Complete the code below.
# ```
# # create 3 variables a,b & c 
# # assign 1 as value to all variables in the same statement
# # incorrect answer if it is 
# a=1 b=1 c=1
# ```
# ```
# #print a
# #print b
# #print c
# ```
# 

# In[11]:


a = b = c = 1
print(a)
print(b)
print(c)


# **Task 5:** Use for and if to find and print all names from list that are at least 5 characters long.
# ```
# names = ["Alice", "Bob", "Charlie", "Dave", "Emily"]
# for # Loop through the list of names
#     # Print all names that are 5 characters or longer
#     # Use len method to find length of the string
#     ```

# In[14]:


names = ["Alice", "Bob", "Charlie", "Dave", "Emily"]
for nm in names:
    if len(nm) >= 5:
        print(nm)


# **Task 6:** Create a list named mylist and include 5 different data items.
# ```
# mylist =   # it should contain 5 different data items, e.g. mylist = ['Apple', 2, 3.1415, 'd', 1024 ]
# print() # print the entire list
# print() # print only the second element, note that the first element index is 0
# #use append to add one more item to your list 
# print() #print the entire list
# ```

# In[18]:


mylist = ['Apple', 2, 3.1415, 'd', 1024 ]
print(mylist)
print(mylist[1])
mylist.append('new friend')
print(mylist)


# **Task 7:** Tuple
# ```
# courses = ("Introduction to Basics for Embedded Python", Python Basics for IoT, "Python Project")
# print() #use len method to print the number of items(courses) in the tuple courses.
# print() #print all items in the tuple courses
# print() #print the third item in the tuple
# ```

# In[23]:


courses = ("Introduction to Basics for Embedded Python", "Python Basics for IoT", "Python Project")
print(len(courses))
print(courses)
print(courses[2])


# **Task 8:** Dictionary
# ```
# #create a dictionary named test with the keys 'course', 'time' and 'ects' and set values as 'Python Basics', 'Autumn', 5
# test = {
#     
# }
# print() #use get method to print the value of the course
# test[] =  #change the course value to Python Basics for IoT
# 
# test[] = #add the key/value pair as year:2020 to the test dictionary
# print() #print the entire dictionary
# #use pop method to remove time form the dictionary
# print() #print the dictionary
# ```

# In[39]:


test = {'course': 'Python Basics', 'time': 'Autumn', 'ect': 5}
print(test.values())
print(test.get('course'))
test['course'] = 'Python Basic for IoT'
print(test)
test['year'] =2020
print(test)
test.pop('time')
print(test)


# **Task 9:** Create Integer, String and Floating point number
# 
# The target of this exercise is to create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.
# Test your variables using print so that program prints variable only if it contains specifig value.Ǹote that you have to use indentation between if-clauses.
# Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces. For example:
# ```
# x = 1
# if x == 1:
#     # indented four spaces
#     print("x is 1.")
# ```
# 
# Test code like that way:
# ```
# if mystring == "hello":
#     print("String: %s" % mystring)
# ```

# In[64]:


mystring = "hello world!"
myfloat = 110.0
myint = 220
if 'hello' in mystring:
    print("String:", mystring)
if '10.0' in str(myfloat):
    print("float: ", myfloat)
if str(myint).find('20'):
    print("int: ", myint)


# #### Example solutions task 9
# 
# <details><summary>CLICK ME</summary>
# <p>
# 
# ```
# mystring = "hello"
# myfloat = 10.0
# myint = 20
# 
# # testing code
# if mystring == "hello":
#     print("String: %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("Float: %f" % myfloat)
# if isinstance(myint, int) and myint == 20:
#     print("Integer: %d" % myint)
# 
# ```
# </p>
# </details>

# **Task 10:** Convert Celsius to Fahrenheit
# 
# The target of this exercise is to code Python Program which take the temperature in Celsius and convert it to Fahrenheit. 
# 
# **Problem Solution**
# 
# 1. Take the value of temperature in Celsius and store it in a variable. Ask user temperature value and store it in int or float type variable.
# 2. Convert it to Fahrenheit. Using the formula of: f=(c*1.8)+32, convert Celsius to Fahrenheit.
# 3. Print the final result.
# 4. Exit.

# In[27]:


temp_cel = float(input("Enter the temperature in celcius: "))
temp_fah = (temp_cel * 1.8) + 32
print ("Temperature in Fahrenheit is:", temp_fah)


