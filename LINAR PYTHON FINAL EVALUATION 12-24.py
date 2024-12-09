"""FINAL EVALUATION
PYTHON PROGRAMMING LANGUAGE
DURATION: 1:45 MINS
Instructions: Answers 7 questions, Number 1, 5 and 9 is compulsory, Pick any 4 others. 
Remember, this evaluation has a lot to do with your certification.

"""
"""
You are advised not to cheat in any for, its an advice and not a must, since it’s not a must you get certified too.  
1)	Variable Data Types 
a) Create a variable called "Date_Of_Birth" and assign it the year you were born (or any random year) using the right datatype. Print the value of the variable. 
b) What is the difference between an integer and a floating-point number in Python? Backup your explanation with an example for each.
c) Explain the types of Logical operators with scenerios.

# QUestion 1 answer goes in here:
"""
Date_of_birth = "17 february 2024"
print(Date_of_birth)

# An integer doesnt have a decimal point while a floating point has a decimal point
example = int = 12,1,2
float = 1.2, 2.5, 3.2

# and operator = This is a type of logical operator that helps to add up two or more statement 
# scenerio: i am a boy "and" i am tall 

# or operator: This is another type of logical operator that helps to make decision
# senerio: should we play football or play basketball

# not operator: this is another type of logical operator that helps to differentiate 
# scenerio: That notebook belongs to me and not you
"""
2)	Basic Operations 
a) Write a Python program that adds two numbers together and prints the result. 
b) Write a Python program that takes a number as input and multiplies it by 10. Print the result.



# QUestion 2 answer goes in here:

"""
first_number = 3
second_number = 2
result = first_number + second_number
print(result)

user_number = int(input("enter a number from range 1-5"))
result = user_number * 10
print(result)

"""
3)	Control Structures 
a) Write a Python program that checks if a number is even or odd. If the number is even, print "Even", otherwise print "Odd". 
b) Write a Python program that takes a number as input and checks if it is positive, negative, or zero. Print the result.




# QUestion 3 answer goes in here:

"""
for x in range(1, 101):
    user_choice = int(input("enter a number of your choice from range 1-100"))
    if user_choice in range(1, 101, 2):
        print("even")
    elif user_choice in range(2, 101, 2)    :
        print("odd")
    else:
        print("enter the right value")


for number in range(1, 51) and range(-1, -51):
    user_choice = int(input("enter a number from range 1-50"))
    if user_choice in range(1, 51):
        print("positive")
    elif user_choice in range(-1, -51)    :
        print("negative")
    elif number == 0:
        print(0)
    else:
        print(None)


"""
4)	Lists, Loops and Data Structure
a) Create a list of numbers from 1 to 10. Print each number in the list using a loop. 
b) Write a Python program that takes a list of numbers as input and returns the sum of all the numbers in the list.
c) Create a dictionary ‘colleague_name’ storing all your colleague names. Hint: Use sequence of numbers as their key.  





# QUestion 4 answer goes in here:

"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print(list[7])
print(list[8])
print(list[9])


first_number-number = int(input("enter a number"))
sp_number = int(input("enter a number"))
tp_number = int(input("enter a number"))
fop_number = int(input("enter a number"))

sum_of_numbers = first_number + sp_number + tp_number + fop_number
print(sum_of_numbers)



"""
5)	Functions 
a) Write a Python function that takes three numbers as input and return their multiplication. 
b) Write a Python function that takes a list of numbers as input and returns the average of all the numbers in the list.
c) Greet a User: Write a function greet_user(name) that takes a person's name as input and returns a greeting message.
Example: Output: "Hello, Alice! Welcome!"
d) Calculate Simple Interest: Write a function simple_interest(principal, rate, time) that calculates simple interest.
Example: Input: simple_interest(1000, 5, 2)
Output: 100.0

e) Convert Minutes to Seconds: Write a function minutes_to_seconds(minutes) that converts a given number of minutes into seconds.
Example:
Input: minutes_to_seconds(5)
Output: 300





# QUestion 5 answer goes in here:

"""
first_numbers = input("enter a numbers")
second_number = input("enter a numbers")
third_number = input("enter a numbers")
result = first_number * second_number * third_number
print(result)


enoch_number = ("input a numbers")
joy_number = ("input a numbers")
peace_number = ("input a numbers")
dam_number = ("input a numbers")
samson_number = ("input a numbers")

average_number = enoch_number + joy_number + peace_number + dam_number + samson_number / 5  #divided by the total number
print(average_number)


def greet_user(name):
    return (f"Hello, Alice! Welcome!")
name = input("enter your name")
print(f"hello, Alice! Welcome!")


def simple_interest(principal, rate, time):
    simple_interest(2000, 4, 2)
    result = 2000 * 4 / 2 * 100
    return result 


def minutes_to_seconds(minutes):
    #mintes to seconds is 60 multiplied by the number in minutes
    given_number = int(input("enter a number in minute"))
    result = given_number * 60
    return result


"""

6)	Libraries and Modules 
a) Install and Import the "math" module and use its "sqrt" function to calculate the square root of a number. 
b) Install and Import the "random" module and use its "randint" function to generate a random number between 1 and 10.
c) Install and Import the "pywhatkit" module and use its "whatsapp" function to send a DM to your tutor with the body “Good Day Sir”



# QUestion 6 answer goes in here:

"""
# pip install math
# from math import sqrt
# sqrt(5)

# pip install random
# import random
# random.randint(1, 10)

# pip install pywhatkit
# import pywhatkit
# pywhatkit.whatsapp("Good Day Sir")
"""
7)	 Explain the following terms relating to Python programming Language with examples where needed
a)	Escape Sequence
b)	Keywords
c)	Datatypes
d)	Dictionary 
e)	Module
f)	Interpreter
g)	Give a brief history of python, who built it, what led to Python and others, state the current version of python you are using.




# QUestion 7 answer goes in here:

"""


"""
8)	Mentions some tools used the career listed below, write extensively on the career you are choosing after this course. Explain what the career entails and the problem skilled professionals in the career solve in the real-world market.
a)	Data Scientist
b)	Software Engineer
c)	Data Engineer
d)	Data Analytics
e)	Web Developer (Backend Developer)
f)	Machine Learning Engineer




# QUestion 8 answer goes in here:

"""


"""
9)	Give a feedback on this Python course, your instructor and this examination.


Question 9 answer goes in here:
This python course has been a great experience so far and it is helpful. it helps me understand python andf know more
about python and how to work with python.

My instruction is a very cool, nice, good, caring, loving and lovely man. He teaches well and makes sure we understand it
and also attends to our problems. He taught me well and he has a great impact in my life.

This examination is a great one, it gives me the priviledge to write codes on my own and know how good i am in coding.
i am hoping to pass this examination and get my certificate and make my parent proud.

IN GOD I TRUST!!!

BEST OF LUCK
"""