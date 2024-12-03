import requests #import requests package

response = requests.get('http://api.open-notify.org/astros.json') #requesting the data from the site and store the data in the response variable
json = response.json() #decode the json and save it in a variable called json
print('The People currently in spaces are:')
for person in json['people']: #looping through and listing all people 1 by 1
    print(person['name']) #printing the list out and choosing the name only by selecting the key
    