# Project Prompt:

# You are hired to build a Student Lookup Tool for a school front office. The secretary must be able to:

    # Enter a student’s full name

    # Instantly see:

            # CPS ID

            # Homeroom

            # Grade Level

            # Primary Email

            # Students must:

            # Describe the search process

## be able to add new data
# Your program must allow the secretary to ADD a brand new student
# into the system while the program is running.

# Your job is to let the secretary type in a new student just like filling out a registration form.
# Once the form is complete, your program must turn that information into a dictionary and add it to the main list of students.
# If the student already exists (same CPS ID), your program must block the entry to prevent duplicates.

# The program should:
    # 1. Ask the user for the following information:
    #    - CPS ID
    #    - First Name
    #    - Last Name
    #    - Middle Name
    #    - Homeroom
    #    - Grade Level
    #    - Primary Email
    #    - Secondary Email

# 2. Combine the First and Last name into this format:
    #    "Last, First"  

# 3. Store all of the new information into ONE dictionary
    #    that matches the structure of the existing student data.

# 4. Add (append) that new dictionary into the main students list.

# 5. After adding the student, the program must:
    #    - Print a confirmation message
    #    - Print the total number of students in the system
    #    - Print the newly added student record

# 6. The program must NOT delete or overwrite any existing students.

# 7. If the CPS ID already exists in the system:
        #    - Do NOT add the student
        #    - Display an error message saying the CPS ID is already taken


import student_data2
students = student_data2.students
print("---Student Registration Form---")
cps_id = input("Enter CPS ID of student: ")
fname = input("Enter First Name of student: ")
lname = input("Enter Last Name of student: ")
mname = input("Enter Middle Name of student: ")
hr = input("Enter Homeroom of student: ")
gl = input("Enter Grade Level of student: ")
primary_email = input("Enter Primary Email of student: ")
secondary_email = input("Enter Secondary Email of student: ")

combo_name = f"{lname}, {fname}"
print("---Processing Registration---")
is_duplicate = False

for student in student_data2.students:
    if cps_id == student["CPSID"]:
        is_duplicate = True
        print("CPS ID already exsists. Student won't be added.")
        break

if not is_duplicate:
    new_student = {
        "CPSID": cps_id,
        "Combo,Name": combo_name,
        "LName": lname,
        "FName": fname,
        "MName": mname,
        "HR": hr,
        "GL": gl,
        "Email": [primary_email, secondary_email]
    }
student_data2.students.append(new_student)
print("Student has been added successfully.")
print("---Registration Complete---")
print("Total students: ",len(student_data2.students))
print(new_student)