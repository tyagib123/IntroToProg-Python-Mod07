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

![image](https://user-images.githubusercontent.com/94503382/144196642-af26d152-c438-4c6d-9902-95e3d23f7fe5.png)

Figure 1. Reading data from the file

- Add_more_data_to_student_file (name, course, studentList): The purpose of this method is to add new student name and course in the studentList after checking whether the provided student name and course are of type string. The code has been wrapped in try block. The method takes in name, course and studentList as input parameters. In the try block, the logic is to check whether the provided student name and course is of type string. If it is of type string then create row and add the row into the existing studentList. If not, the exception will be raised by calling ValueException () method of ExceptionStudentCls. There is another general exception which gets raised on checking whether the name and course is of type. Overall, two exceptions are raised together in block of code. Finally, we return studentList as result. The complete method logic is shown in Figure 2.

![image](https://user-images.githubusercontent.com/94503382/144196090-1c56fb8e-6ec5-4fbd-8af5-1fc0fe0617dd.png)

Figure 2. Adding new student data in studentList

- Write_and_save_data_to_new_file (newStuFileName, studentList): The purpose of this method is to save the student data to a new file named as RawStudentDirectory.txt. The method starts with try block that contains logic where we first take the file name where user wants to write the data. Then, we check whether the user provided file name is similar to what has been mentioned in the code initially i.e., RawStudentDirectory.txt. If the file names are same then we open the new file in write mode and iterate through each row in the studentList and write it to the new file. In case if the file names are different, then we raise general exception with message “The file is not same”. Another exception is raised in except block which calls CustomException () of ExceptionStudentCls with message “CustomError: Please use the correct file name!”. Finally, we return studentList as a result. The complete method logic is shown in Figure 3.

![image](https://user-images.githubusercontent.com/94503382/144196517-6aeff7f9-b471-45a3-9013-cf348613f4a0.png)

Figure 3. Saving data in new file

- Pickle_student_data (binaryStuFileName, studentList): The purpose of this method is to convert the list object into byte streams. This method takes file name where we want to store the data in binary format along with studentList. The logic starts with opening the file in wb mode (i.e., write + binary) mode. Finally, we use dump () method which takes two parameters i.e., studentList and binaryFile which is a file object. After writing all rows of the studentList, we close the file using close (). The complete method logic is shown in Figure 4.

![image](https://user-images.githubusercontent.com/94503382/144196679-12b1f3aa-0f81-42a1-ba7c-c2aa313506a8.png)

Figure 4. Pickling data logic

- Unpickle_student_data (binaryStuFileName): The purpose of this method is to convert the byte streams back to list object. This method takes binary file name as an input parameter. We again open the file in read + binary mode and finally use load () to read the binary file in text format. The complete method logic is shown in Figure 5.

![image](https://user-images.githubusercontent.com/94503382/144196806-fd5a038c-7680-4656-929c-eebad9754dc1.png)

Figure 5. Unpickling data logic

2. IOStudentProcessor class methods:

- Print_menu_student_tasks (): The purpose of this method is to print the menu options. The complete logic is shown in Figure 6.

- Input_menu_choice (): The purpose of this method is to get the user choice among the provided student menu options. As a result, we return choice of the user. The complete logic is shown in Figure 6.

- Print_current_student_tasks (): The purpose of this method is to print the current student objects in the studentList.  The complete logic is shown in Figure 6.

- Input_yes_or_no_choice (): The purpose of this method is to return the message in terms of y/n when the logic asks user whether they want to continue with the instructions to finish the tasks. The complete logic is shown in Figure 6.

- Input_new_name_and_course (): The purpose of this method is to take new student name and course from user as input and return both parameters as a result. The complete logic is shown in Figure 6.

