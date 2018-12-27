import os
import sys
import requests
import json



ACCUWETHER_TOKEN = os.environ['AWTOKEN']
LOCATION_KEY='324561'
CURRENT_CONDITION_URL='http://dataservice.accuweather.com/currentconditions/v1/'

##### For testing
def write_json(data, filename='answer.json'):
	with open(filename, 'w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)
##### End testing


def get_current_weather_all_data (weather_token, location='324561'):
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
all_data = get_current_weather_all_data(weather_token=ACCUWETHER_TOKEN)

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

write_json(get_current_weather_all_data(weather_token=ACCUWETHER_TOKEN))

weather = "The weather is %s" % (get_weather_text(all_data))
icon = "Icon is %s" % (get_icon_id(all_data))
temperature = "Temperature is %s" % (get_current_temperature(all_data))
real_feel_temperature = "Real feel Temperature is %s" % (get_current_feel_real_temperature(all_data))
wind_speed = "Wind speed is %s" % (get_current_wind_speed(all_data))

def all_info():
	all = '''
		The weather is %s
		Temperature is %s
		Real feel Temperature is %s
		Wind Speed is %s
	''' % (get_weather_text(all_data), get_current_temperature(all_data), \
		   get_current_feel_real_temperature(all_data),get_current_wind_speed(all_data))
	return all
