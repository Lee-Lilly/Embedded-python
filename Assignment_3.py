#!/usr/bin/env python
# coding: utf-8

# ---
# # Python Basics - Assingment 3 ToDo
# 
# ---
# **Exercise 1**
# 
# **Task 1** Define a function called **repeat_stuff** that takes in two inputs, **stuff**, and **num_repeats**.
# 
# We will want to make this function print a string with stuff repeated num_repeats amount of times. For now, only put an empty print statement inside the function.
# 

# In[6]:


def repeat_stuff(stuff, num_repeats):
    for i in range(num_repeats):
        print(stuff)

repeat_stuff (input("Input an word: "), int(input("Repeat how many times? ")))


# ---
# **Task 2** Outside of the function, call repeat_stuff.
# 
# You can use the value "Row " for stuff and 3 for num_repeats. 
# Change the print statement inside repeat_stuff to a **return** statement instead. It should **return stuff*num_repeats**
# Note: Multiplying a string just makes a new string with the old one repeated! For example: "na*6 -> result is nanananana
# Then, give the parameter **num_repeats** a default value of **10**.

# In[7]:


def repeat_stuff(stuff, num_repeats):
        return stuff*num_repeats

repeat_stuff (input("Input an word: "), int(input("Repeat how many times? ")))  


# ---
# **Task 3** Add **repeat_stuff("Row ", 3)** and the string **"Your Boat. " ** together and save the result to a variable called **lyrics**.
# 
# Create a variable called **song **and assign it the value of **repeat_stuff** called with the singular input **lyrics**.
# 
# Print song.
# 
# Good job!!

# In[14]:


def repeat_stuff(stuff, num_repeats):
        return stuff*num_repeats
lyrics = repeat_stuff("Row ", 3) + "Your Boat! \n"
song = repeat_stuff(lyrics, 3)
print(song)


# ---
# **Exercise 2**
# 
# The program reads the height in centimeters and then converts the height to feet and inches.
# 
# Problem Solution
# 
# 1. Take the height in centimeters and store it in a variable.
# 2. Convert the height in centimeters into inches and feet.
# 3. Print the length in inches and feet.
# 4. Exit.
# 
# Hint! 
# inches=0.394*cm
# feet=0.0328*cm

# In[1]:


def cm_feet(figure):
    return round(figure/30.48, 2)

height = float(input("Enter your height in cm: " ))
res = cm_feet(height)
print("You are ", res, "feet tall.")


# ---
# **Exercise 3**
# 
# This is a Python Program to check whether a number is positive or negative.
# 
# Problem Solution
# 
# 1. Take the value of the integer and store in a variable.
# 2. Use an if statement to determine whether the number is positive or negative.
# 3. Exit.

# In[1]:


def evaluate(num):
    if num < 0:
        print(num, "is negative.")
    elif num > 0:
        print(num, "is positive.")
    elif num == 0:
        print(num, "is zero.")

num = int(input("Enter an integer: "))
evaluate(num)


