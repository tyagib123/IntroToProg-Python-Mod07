# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with Exception Handling and picking in the python script. When program starts, it will load
# each row of students data in "StudentDirectory.txt" into a python dictionary. Add each dictionary row to python list
# Also, this script handles exceptions and pickling to write and read the data in/from binary format.
# ChangeLog (Who,When,What):
# Bhawna,1.1.2030,Created started script
# -------------------------------------------------------------#

import pickle
strFileName = "StudentDirectory.txt"  # Source file for reading the existing student data
newStuFileName = "RawStudentDirectory.txt"  # New source file for saving the student data
binaryStuFileName = "BinaryStuDir.dat"  # File in binary format for storing pickling result.
objFile = None  # an object to read source file and new file in text format.
binaryFile = None  # an empty object to read and write student data in binary format.
studentList = [] # an empty list to store student dictionary objects.
strChoice = ""  # variable to store user input
StuName = ""  # variable to store key (student name) in student dictionary.
StuCourse = ""  # variable to store value (student course) in student dictionary.
strStatus = ""  # variable to track the status (i.e., y/n) for user.


# Processing of the student directory
class StudentProcessor:

    # Reads student data from StudentDirectory.txt file
    def read_data_from_student_file(strFileName, list_of_rows):
        objFile = open(strFileName, 'r')
        for row in objFile:
            name, course = row.split(',')
            row = {"StuName": name.strip(), "StuCourse": course.strip()}
            studentList.append(row)
        objFile.close()
        return studentList

    # Adds more student data in StudentDirectory.txt file
    @staticmethod
    def add_more_data_to_student_file(name, course, studentList):
        try:
            # If the name/course of the student is of type int then raise an exception.
            if name.isdigit() or course.isdigit():
                raise Exception("Key or value should be of type string.")
            # If the name/course of the student is not of type int then add it to the student list.
            else:
                StudentRow = {"StuName": str(name).strip(), "StuCourse": str(course).strip()}
                studentList.append(StudentRow)
            # Call ExceptionStudentCls method to handle the value exception.
        except Exception as e:
            ExceptionStudentCls.ValueException()
            return studentList

    # Save data to a new file
    @staticmethod
    def write_and_save_data_to_new_file(newStuFileName, studentList):
        # Check if the provided file name by user is equal to the file name that we created for saving the student
        # data. If not, raise custom exception asking user to use the correct file name to store the data.
        # If the file name is similar, the start writing data to the file.
        try:
            fileName = str(input("Please enter the new file where you want to save the students data."))
            if fileName != newStuFileName:
                raise Exception("The file is not same.")
            else:
                objFile = open(newStuFileName, 'w')
                for row in studentList:
                    objFile.write(row["StuName"] + "," + row["StuCourse"] + "\n")
                objFile.close()
        # Call ExceptionStudentCls method to handle the custom exception.
        except Exception as e:
            ExceptionStudentCls.CustomException()
        return studentList

    # Pickling of the students data
    @staticmethod
    def pickle_student_data(binaryStuFileName, studentList):
        # Open binarystuFileName in write and binary mode and write the students data in binary format using dump().
        with open(binaryStuFileName, 'wb') as binaryFile:
            pickle.dump(studentList, binaryFile)
        binaryFile.close()

    # Unpickling of the students data
    def unpickle_student_data(binaryStuFileName):
        # Open binaryStuFileName in read and binary mode to reload the students data using load().
        with open(binaryStuFileName, 'rb') as readbinaryFile:
            print(pickle.load(readbinaryFile))



# I/O as well as exception handling of students data
class IOStudentProcessor:

    # Show the student menu options to the user
    @staticmethod
    def print_menu_student_tasks():
        print('''
        Menu of Options
        1) Add new student name and course
        2) Save data to a new student file
        3) Pickle the student data
        4) Unpickle the student data
        5) Exit from the program
        ''')
        print()

    # Gets the user choice from the menu options
    @staticmethod
    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()
        return choice

    # Show current student data
    def print_current_student_tasks(studentList):
        print("******* Current Student Directory: ******* ")
        for row in studentList:
            print(row["StuName"] + "," + row["StuCourse"])

    def input_yes_or_no_choice(message):
        return str(input(message)).strip().lower()

    def input_press_to_continue(optional_message=''):
        print(optional_message)
        input("Press Enter to continue.")

    # Gets user input for new student name and course
    @staticmethod
    def input_new_name_and_course():
        name = str(input("Enter new student name: "))
        course = str(input("Enter new student course: "))
        return name, course

# Exception class for handling different exception types.
class ExceptionStudentCls:

    @staticmethod
    def ValueException():
        # Handles ValueError exception
        raise ValueError("Value should be of string type not int/float/bigint")

    @staticmethod
    def CustomException():
        # Handles Custom exception
        raise Exception("CustomError : Please use the correct file name!")


# Main body of the script
# Step 1: Load student data from StudentDirectory.txt when the program starts
res = StudentProcessor.read_data_from_student_file(strFileName, studentList)
print(res)


# Step 2: Display a menu of choices to the user
while (True):
    # Step 3: Show current students data and gets the user choice
    IOStudentProcessor.print_current_student_tasks(studentList)
    IOStudentProcessor.print_menu_student_tasks()
    strChoice = IOStudentProcessor.input_menu_choice()

    # Step 4: Process user's student menu choice
    if strChoice.strip() == '1':
        # Add new student name and course in the existing Student List.
        print("***** Add operation called on student list *****")
        name, course = IOStudentProcessor.input_new_name_and_course()
        new_names_courses_to_list = StudentProcessor.add_more_data_to_student_file(name, course, studentList)
        IOStudentProcessor.input_press_to_continue(strStatus)
        continue

    elif strChoice == '2':
        print("****** Saving data to the file *******")
        save_data_to_file = IOStudentProcessor.input_yes_or_no_choice("Save data to a new file? (y/n) - ")
        if save_data_to_file.lower() == "y":
            list_of_students = StudentProcessor.write_and_save_data_to_new_file(newStuFileName, studentList)
            IOStudentProcessor.input_press_to_continue(strStatus)
        else:
            IOStudentProcessor.input_press_to_continue("Data is not saved to a new file!")
        continue

    elif strChoice == '3':
        print("***** Pickle the student list in binary format *******")
        StudentProcessor.pickle_student_data(binaryStuFileName, studentList)
        IOStudentProcessor.input_press_to_continue(strStatus)
        continue

    elif strChoice == '4':
        print("***** Unpickle the student list present in binary format ******")
        StudentProcessor.unpickle_student_data(binaryStuFileName)
        IOStudentProcessor.input_press_to_continue(strStatus)
        continue

    elif strChoice == '5':
        print("****** Exiting the program ********")
        print("Good bye!")
        break
