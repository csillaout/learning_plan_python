import requests
city = "London"
url = "http://api.weatherapi.com/v1/current.json?key=131f8c2fdca84b329d192835242711&q="+city+"&aqi=no"

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c') #this is how we get the temp in celsius and assign it to a variable
condition = weather_json.get('current').get('condition').get('text')
print(weather_json)
print(weather_json['current']['condition']['text']) #clear
print(weather_json['current']['temp_c']) #temp in celcious
print(temp)
print(condition)
print(f"Today's weather in {city} is {condition.casefold()} with {temp}°C.") #using f-string is cleaner and more modern approach

