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

### Different methods within each class:
1.	StudentProcessor class methods:

- Read_data_from_file (strFileName, list_of_rows): The purpose of this method is to read the file which has student data. Basically, this file contains student names and courses as rows separated by comma and create dictionary object. Finally, create list of student dictionary objects. This method takes file name that contains student data and student list. The function starts with opening the file in the read mode and then split the student row using split (). On splitting the row, we will store student name in name variable and student’s corresponding course in course variable. Using these two variables, we create row and finally add that row in the studentList. This list i.e., (studentList) has been initialized as an empty list to store the dictionary objects. After adding all student names and courses in a list, we close the file and return studentList as result. The complete method logic is shown in Figure 1.

 
Figure 1. Reading data from file

![image](https://user-images.githubusercontent.com/94503382/144195805-c5802ec5-4690-4235-bcdc-13408d930227.png)

