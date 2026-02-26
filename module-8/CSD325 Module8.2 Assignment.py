#Girma Dingeto
# CSD325 Module 8.2 Assignment

import json
import os
from os import path

#Define filename
students='student.json'
data = []

#Function Definition
def print_students(student_list):
    """Print the list of students with a message."""

jason_string = '''
{
  "students": [
    {
      "F_Name": "Ellen",
      "L_Name": "Ripley",
      "Student_ID": 45604,
      "Email": ["eripley@gmail.com"]
    },
    {
      "F_Name": "Arthur",
      "L_Name": "Dallas",
      "Student_ID": 45605,
      "Email": ["adallas@gmail.com"]
    },
    {
      "F_Name": "Joan",
      "L_Name": "Lambert",
      "Student_ID": 45714,
      "Email": ["jlambert@gmail.com"]
    },
    {
      "F_Name": "Thomas",
      "L_Name": "Kane",
      "Student_ID": 68554,
      "Email": ["tkane@gmail.com"]
    }
  ]
}
'''
data=json.loads(jason_string)


   
for student in data["students"]:
        # Adjust keys['L_Name'] and ['F_Name'] to match the actual keys in your JSON data
        print(f" {student['L_Name']}, {student['F_Name']} :"
              f"ID = {student['Student_ID']} ,Email= {student['Email']}")
            
     
       
print(f" This is Students original lists.")

#3 .Append new student data to the list ( replace with your information)

students = 'students.json'
data = []

    #1. Use JSON load() to load file into a list
if path.isfile(students) is False:
        raise Exception(f"Error: {students} does not exist.")
else:
        with open(students) as json_file:
            data = json.loads(json_file)
    
data.append({
        "F_Name": "Tom",
        "L_Name": "Hanks",
        "Student_ID": 45606,
        "Email": ["thanks@gmail.com"]
    })
     
    
    #4. Output the updated list of students and call functions to print the list
print("\n---This is the Updated Student List---")
print(data)
        
#main program
def main ():
    
            
    #2. Output the original list of students and call functions to print the list
    print("\n---This is the Original Student List---")
    print(data)

    

    #5. Use JSON dump() to save the updated list back to the file
    with open(students, 'w') as json_file:
        json.dump(data, json_file, indent=4)

        
    #6. Print a message confirming that the file has been updated
    print(f"\nNotification: {students} has been updated with new student data.")

    if __name__ == "__main__":
        main() 
        

        



      

    