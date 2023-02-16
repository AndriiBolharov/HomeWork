"""
Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents.
Run your two scripts from the system command line.
Does the new file show up in the directory where you ran your scripts?
What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings; add an explicit ‘\n’ at the end of the string
if you want to fully terminate the line in the file.
"""
print("Task 1")

with open("mytext.txt", "w") as my_text:
    my_text.write("Hello file world")

with open("mytext.txt", "r") as my_text:
    text = my_text.read()
print(text)
print("\n")

"""
Extend Phonebook application
Functionality of Phonebook application:
Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.
"""
print("Task 2")
import json
from pprint import pprint

filepath = "./information.json"

with open(filepath) as file:
    user_raw = file.read()
user_list: list = json.loads(user_raw)
pprint(user_list)

for user in user_list:
    first_name = user.get("First_name")
    print("First_name:" f"{first_name}")


for user in user_list:
    last_name = user.get("Last_name")
    print("Last_name:" f"{last_name}")


for user in user_list:
    full_name = user.get("Full_name")
    print("Full_name:" f"{full_name}")

for user in user_list:
    PhoneNumber = user.get("PhoneNumber")
    print("PhoneNumber: " f"{PhoneNumber}")

for user in user_list:
    city = user.get("City")
    print("City: " f"{city}")

# pos = int(input())
# with open(filepath, "w+") as number:
#     L = number.readlines()
# if (pos >= 0) and (pos < len(L)):
#     i = pos
#     while i<len(L)-1:
#         L[i] = L[i+1]
#         i = i+1
#     L = L[:-1]








