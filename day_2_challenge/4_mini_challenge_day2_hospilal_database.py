# Do not do this on week 17 day one, this will be done day 2

# What This Hospital Challenge Teaches

# Students will practice:

#     Dictionaries inside lists

#     Searching by key/value

#     Adding new records

#     Updating records safely

#     Deleting records

#     Preventing duplicate IDs

#     Real-world database logic used in hospitals, insurance, and EMR systems

# #########################Scenario##############################
# You are building a real hospital patient system.
# Nurses must be able to search, add, update, and discharge patients safely.
# Every patient must be stored as a dictionary and placed inside a list.
# The hospital depends on your program to keep critical patient data accurate.

# -----------------------------------------------
# Project Prompt: Hospital Patient Lookup System
# -----------------------------------------------

# You are hired to build a Patient Lookup Tool for a hospital front desk.
# Nurses and doctors must be able to quickly find and manage patient records.

# The system must allow the nurse to:

# 1. Enter a patient's full name
#    (Format entered by user: First Last)

# 2. Instantly see the following patient information:
#    - Patient ID
#    - Age
#    - Room Number
#    - Assigned Doctor
#    - Triage Level
#    - Current Status (Waiting, In Treatment, Discharged)
#    - Primary Contact Email

# -----------------------------------------------
# You must:
# -----------------------------------------------

# - Describe the search process in plain English
# - Explain what key is being searched
# - Explain what value is being returned
# - Explain what happens if the patient is NOT found

# -----------------------------------------------
# be able to add new data
# -----------------------------------------------

# Your program must allow the nurse to ADD a brand new patient
# into the hospital system while the program is running.

# The program should:
# 1. Ask the user for the following information:
#    - Patient ID
#    - First Name
#    - Last Name
#    - Age
#    - Room Number
#    - Assigned Doctor
#    - Triage Level (1 = Critical, 5 = Minor)
#    - Current Status (Waiting / In Treatment / Discharged)
#    - Primary Contact Email
#    - Secondary Contact Email

# 2. Combine the First and Last name into this format:
#    "Last, First"

# 3. Store all of the new information into ONE dictionary
#    that matches the structure of the existing patient data.

# 4. Add (append) that new dictionary into the main patients list.

# 5. After adding the patient, the program must:
#    - Print a confirmation message
#    - Print the total number of patients in the system
#    - Print the newly added patient record

# 6. The program must NOT delete or overwrite any existing patients.

# 7. If the Patient ID already exists in the system:
#    - Do NOT add the patient
#    - Display an error message saying the Patient ID is already taken

# -----------------------------------------------
# be able to update patient data
# -----------------------------------------------

# The system must allow the nurse to UPDATE existing patient information.

# The program should allow updates for:
# - Room Number
# - Assigned Doctor
# - Patient Status

# The nurse must:
# 1. Enter the Patient ID
# 2. Choose which field to update
# 3. Enter the new value
# 4. See the updated patient record printed to the screen

# -----------------------------------------------
# be able to discharge a patient
# -----------------------------------------------

# When a patient is discharged:
# - The nurse must enter the Patient ID
# - The patient must be completely removed from the system
# - A confirmation message must be displayed
# - The total patient count must update correctly

# -----------------------------------------------
# safety & data integrity rules
# -----------------------------------------------

# - No two patients may share the same Patient ID
# - Every patient MUST have:
#   - An ID
#   - A Full Name
#   - A Status
#   - A Triage Level
# - The program must not crash if the nurse types a name incorrectly
# - The program must display a clear error message instead
