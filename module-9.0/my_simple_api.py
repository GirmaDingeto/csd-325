
import requests
import json
api_url="https://randomuser.me/api/"

#b.Test the connection of my API, output results
# status code=200 means success
response=requests.get(api_url)
print(f"API connection status code: {response.status_code}\n")

# c. print out the unformated response from the request
# the response.text attribute gives unformated JSON string

print("Unformated JSON Response \n ")
print(response.text,"\n")





#Print the formated response
#Parse the JSON into a Python dictionary and print formated information
def jprint(obj):
    if response.status_code==200:
       data=response.json()
   # user_info=data['results'] #Get the first user in the resulted list

       print("Formatted Output")
       

    else:
        print("coUld not fetch data from custom API")  


# create a formatted string of the Python JSON object
# create a formatted string of the Python JSON object

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())