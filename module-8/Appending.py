
import json
import os 
filename= [
    {
        "F_Name": "Ellen",
        "L_Name": "Ripley",
        "Student_ID": 45604,
        "Email": "eripley@gmail.com"
    },
    {
        "F_Name": "Arthur",
        "L_Name": "Dallas",
        "Student_ID": 45605,
        "Email": "adallas@gmail.com"
    },
    {
        "F_Name": "Joan",
        "L_Name": "Lambert",
        "Student_ID": 45714,
        "Email": "jlambert@gmail.com"
    },
    {
        "F_Name": "Thomas",
        "L_Name": "Kane",
        "Student_ID": 68554,
        "Email": "tkane@gmail.com"
    }
]
filename = "Student.json"
listobj = []

#if path.isfile(filename) is False:
    #raise Exception(f"Error: {filename} does not exist.")

    
with open(filename) as file:
        listobj = json.load(file)

print(listobj)

listobj.append({

        "F_Name": "Tom",
        "L_Name": "Hanks",
        "Student_ID": 45606,
        "Email": ["thanks@gmail.com"]
    })

print(listobj)
     
with open(filename, 'w') as file:
        json.dump(listobj, file, indent=4)      

print(f"\nNotification: {filename} has been updated with new student data.")   
