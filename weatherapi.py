import requests

api_key = "da67ceb77507e6b7267dd221705f610d"

user_input =   input("enter the city:")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")
print(weather_data.json()) 

if weather_data.json()['cod']=='404':
    print("not city found")

else:

    weather  = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(weather,temp)

    print(f"The weather is {user_input} is : {weather}")
    print(f"The temperature is {user_input} is : {temp}")
    # https://youtu.be/baWzHKfrvqw