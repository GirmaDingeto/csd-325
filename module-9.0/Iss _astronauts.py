import requests
import json

# The URL for the current astronats API
url="http://api.open-notify.org/astros"

#Send a GET request to the API
response= requests.get(url)

print(response.status_code,"\n")


#Check the status code (optimal,but good practice)
def jprint(obj):
    if response.status_code==200:
        print("Unformated Output,\n")

        data=response.json()

        print ("Current astronauts ")

    
        print(data,"\n" )
    else:
        print(f"failed to retrieve data.Status code:{response.status_code}")   


# create a formatted string of the Python JSON object
    print("\n Formated output")

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())   