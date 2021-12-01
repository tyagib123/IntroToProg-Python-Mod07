# Structured Error Handling and Pickling
**Dev:** *Bhawna*  
**Date:** *11.30.2021*

## Introduction
This assignment is about understanding and experimenting on how to handle errors/exceptions in python code. As part of this exercise, I have created a case where school admin is going to maintain list of students and in which courses they have enrolled themselves. I will walk you through one example code where I will be creating student list of dictionary objects with student name and their courses as keys. Within the same example, I have introduced pickling which explains how the data can be stored in binary format in python. That being said, in the upcoming sections, I will show you how I have created different classes to performed different operations and the expected exceptions that can happen while performing operations on the list of student dictionaries. 

## What is an exception and exception handling in python?
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program’s instructions. In general, when a python script encounters a situation that it cannot cope with, it raises an exception. An exception is a python object that represents an error. If you have some suspicious code that may raise an exception, you can defend your program by placing suspicious code in a try block. After the try block, you must include an except statement followed by a block of code which handles the exception.

## What is pickling and unpickling in python?
In python, pickle module is used to serialize or deserialize python object structures. The process of converting any python objects (i.e., list, dictionary) into byte streams is called pickling. We can also convert the byte streams back into python objects. This process is known as unpickling.

## Breakdown of python script:

### Different classes to handle Processing/IO tasks and Exception handling:
Below are the three classes that I have created in my python script:

1.	StudentProcessor:
This class is responsible for processing of the below tasks:
a.	Reading student data from the text file
b.	Adding more student dictionary objects in the student list.
c.	Saving the student data to the new file.
d.	Pickling of the student data.
e.	Unpickling of the student data.

2.	IOStudentProcessor: 
This class is responsible for printing out the student menu options as well as getting user input to perform certain tasks using student menu. Following are the tasks:
a.	Gets the user choice from the student menu options.
b.	Show the current student menu options to the user.
c.	Get the user input to add new student name and course.
d.	Asking user to choose from y/n to continue the process or not.

3.	ExceptionStudentCls: 
This class is responsible for handling different exceptions such as TypeError as well as CustomError.
