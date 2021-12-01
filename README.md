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

![image](https://user-images.githubusercontent.com/94503382/144197069-06c230e6-f747-43ee-ac2e-1f1cefcca63c.png)

Figure 6. IOStudentProcessor class methods

3.ExceptionStudentCls class methods:

ValueException (): The purpose of this method is to raise an exception when the provided student name and course is not of type string. The complete logic is shown in Figure 7.

CustomException (): The purpose of this method is to raise custom exception when the provided file name to save the student data is not similar to the one mentioned in the python script. The complete logic is shown in Figure 7.

![image](https://user-images.githubusercontent.com/94503382/144197168-a9a6e24b-daf1-44b2-ab1c-6aecd53eaff0.png)

Figure 7. ExceptionStudentCls class methods

### Main body of the script:
Step 1: The program starts with calling the read_data_from_student_file () in order to load the data from the file as shown in Figure 8.

![image](https://user-images.githubusercontent.com/94503382/144197496-403950ff-4aef-4e25-b85f-c66e88980938.png)

Figure 8. Beginning of the Main script of the body by loading the data from the file

Step 2: Next step is to show the menu options to the user along with getting the user choice. This is done by calling the IOStudentProcessor class methods as shown in Figure 9.

![image](https://user-images.githubusercontent.com/94503382/144197626-d32dd425-ff13-4377-b4c1-be7b5f361f1b.png)

Figure 9. Calling IOStudentProcessor Class methods

Step 3: If the user chooses option 1, this means that user wants to add new student names and enrolled courses in the existing student list. In order to achieve this, first we ask user to provide the student ‘s name and course that needs to be added to the list and finally we call the methods that would do this processing on behalf of the user. Finally, we ask user whether they want to continue with the next action or not. The complete logic is shown in Figure 10.

![image](https://user-images.githubusercontent.com/94503382/144197686-22ccbabc-8212-4eb1-98c7-02782634f4a4.png)

Figure 10. Logic for student menu option 1

Step 4: If user chooses option 2, this means that user wants to save the data to the new file. In order to achieve this, first we ask user whether they want to save the data to the file or not. If the input is ‘y’ then the method would be called which will be responsible for saving the data to the file. Finally, we ask user whether they want to continue with the next action or not. In case, if they don’t want to proceed with saving data to a file, then print the message to the user “Save canceled”. This means that data will not be saved to the file. The complete logic is shown in Figure 11.

![image](https://user-images.githubusercontent.com/94503382/144197828-21fb5971-143c-4008-b386-f0a2e24ac57b.png)

Figure 11. Logic for student menu option 2

Step 5: If user chooses option 3, this means that user wants to convert the data into binary format. If this is the case then we would call pickle’s dump method to achieve this task.  The complete logic is shown in Figure 12.

![image](https://user-images.githubusercontent.com/94503382/144197900-a6ebcddd-6b9b-4222-aa0d-ba45b001d37c.png)

Figure 12. Logic for student menu option 3

Step 6: If user chooses option 4, this means that user wants to convert the data back into list object from binary format. If this is the case then we would call pickle’s load method to achieve this task.  The complete logic is shown in Figure 13.

![image](https://user-images.githubusercontent.com/94503382/144198081-912e6481-da1c-474b-b8cb-6c9b9123dd21.png)

Figure 13. Logic for student menu option 4

Step 7: If the user chooses option 5, this means that user wants to exit from the program. The complete logic is shown in Figure 14.

![image](https://user-images.githubusercontent.com/94503382/144198180-22790e36-5c88-4ac3-b9a6-5272dae78c6f.png)

Figure 14. Logic for student menu option 5

### Execution result in PyCharm:

Scenario 1: Load data while reading the file:

![image](https://user-images.githubusercontent.com/94503382/144198425-b6a907cd-d723-4b3c-9770-3a5667618541.png)

Scenario 1

Scenario 2a: Successful addition of new student and course in the student list:

![image](https://user-images.githubusercontent.com/94503382/144198534-0636180e-8805-473b-91d4-d32a67fac87d.png)

Scenario 2a

Scenario 2b. Exception messages when user wants to add student name or course other than string type:

![image](https://user-images.githubusercontent.com/94503382/144198630-9bc49fbb-7154-42d1-974a-4ec2ae1e5d5d.png)

Scenario 2b

Scenario 3a. Successful saving data in a file:

![image](https://user-images.githubusercontent.com/94503382/144198754-9d03c145-be2a-458a-9014-ff8fd57a1c60.png)

Scenario 3a

RawStudentDirectory.txt content:

![image](https://user-images.githubusercontent.com/94503382/144198811-ecb8be76-e125-4aba-af52-685e7ef5ea8d.png)

Scenario 3b. Exception messages when user provided file name is not similar to initialized in the script with name ‘RawStudentDirectory.txt’.

![image](https://user-images.githubusercontent.com/94503382/144198864-4e5f7312-056f-4ef9-96d1-50d81f28e96b.png)

Scenario 3b

Scenario 4. Pickling of the data:

![image](https://user-images.githubusercontent.com/94503382/144198925-60e48c39-485f-4f9b-af5c-62d9ebec97fc.png)

Scenario 4

BinaryStuDir.dat file content:

![image](https://user-images.githubusercontent.com/94503382/144198984-a8d409d0-1b81-4c47-9509-6706477a40d7.png)

Scenario 5. Unpickling of the data:

![image](https://user-images.githubusercontent.com/94503382/144199022-1b938319-d178-49ad-ac7f-00d2d7748d39.png)

Scenario 5

Scenario 6. Exiting from the program:

![image](https://user-images.githubusercontent.com/94503382/144199158-93c8590b-1497-49da-8b2d-a94cdab70d72.png)

Scenario 6

### Execution result in MacOS:

Scenario 1: Load data while reading the file:

![image](https://user-images.githubusercontent.com/94503382/144199281-8d93451b-4b6e-4929-9e10-609f64965be6.png)

Scenario 1

Scenario 2a: Successful addition of new student and course in the student list:

![image](https://user-images.githubusercontent.com/94503382/144199343-b87893e1-beab-4265-81a2-b0b382d4af68.png)

Scenario 2a

Scenario 2b. Exception messages when user wants to add student name or course other than string type:

![image](https://user-images.githubusercontent.com/94503382/144199399-332332fe-39a0-4f2c-a8b1-21634892bdbe.png)

Scenario 2b

Scenario 3a. Successful saving data in a file:

![image](https://user-images.githubusercontent.com/94503382/144199485-0305450e-8664-4bf8-95ba-52e93903bb22.png)

Scenario 3a

RawStudentDirectory.txt content:

![image](https://user-images.githubusercontent.com/94503382/144199556-1a3c0869-0d26-49a9-8223-91961211ca1b.png)

Scenario 3b. Exception messages when user provided file name is not similar to initialized in the script with name ‘RawStudentDirectory.txt’.

![image](https://user-images.githubusercontent.com/94503382/144199595-102d4022-20b0-4249-a134-5345c78a5f64.png)

Scenario 3b

Scenario 4. Pickling of the data:

![image](https://user-images.githubusercontent.com/94503382/144199668-9507629b-031d-4552-9b0a-a24d43c5cd56.png)

Scenario 4

BinaryStuDir.dat file content:


