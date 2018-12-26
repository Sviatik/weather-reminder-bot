import sys
import requests
import json



#BOT_TOKEN=${BOT_TOCKEN}
BOT_TOKEN='###'
LOCATION_KEY='324561'
CURRENT_CONDITION_URL='http://dataservice.accuweather.com/currentconditions/v1/'
ACCUWETHER_TOKEN='###'

##### For testing
def write_json(data, filename='answer.json'):
	with open(filename, 'w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)
##### End testing


def get_current_weather_all_data (location, weather_token):
##### Real usage 
	url = 'http://dataservice.accuweather.com/currentconditions/v1/' + location + '?apikey=' + weather_token + "&details=true"
	data = requests.get(url)
	content = data.json()
##### End Real

##### For testing
	# with open("test.data.txt", "rb") as fd:
	# 	data = fd.read()				
	# content = json.loads(data)
##### End testing	
	return content

def get_current_temperature (all_data):
	temperature = all_data[0]['Temperature']['Metric']['Value']
	return temperature

def get_current_feel_real_temperature (all_data):
	real_feel_temperature = all_data[0]['RealFeelTemperature']['Metric']['Value']
	return real_feel_temperature

def get_current_wind_speed (all_data):
	wind_speed = all_data[0]['Wind']['Speed']['Metric']['Value']
	speed_unit = all_data[0]['Wind']['Speed']['Metric']['Unit']
	return str(wind_speed) + ' ' + speed_unit

def get_weather_text (all_data):
	weather_text = all_data[0]['WeatherText']
	return weather_text

def get_icon_id (all_data):
	icon_id = all_data[0]['WeatherIcon']
	return icon_id

write_json(get_current_weather_all_data(LOCATION_KEY, ACCUWETHER_TOKEN))
all_data = get_current_weather_all_data(LOCATION_KEY, ACCUWETHER_TOKEN)

print("The weather is ", get_weather_text(all_data))
print("Icon is ", get_icon_id(all_data))
print("Temperature is ", get_current_temperature(all_data))
print("Real feel Temperature is ", get_current_feel_real_temperature(all_data))
print("Wind Speed is ", get_current_wind_speed(all_data))
