import os
import requests
import json
from weather_reminder_bot import *
from time import sleep


TOKEN = os.environ['TGTOKEN']

URL = "https://api.telegram.org/bot" + TOKEN + "/"

def write_json(data, filename='answer.json'):
	with open(filename, 'w') as file:
		json.dump(data, file, indent=2, ensure_ascii=False)

def get_updates():
	url = URL + "getupdates"
	r = requests.get(url)
	return r.json()

def get_message():
	data = get_updates()
	chat_id = data['result'][-1]['message']['chat']['id']
	text = data['result'][-1]['message']['text']
	update_id = data['result'][-1]['update_id']
	message = {'chat_id': chat_id,
			   'text': text,
			   'update_id': update_id}
	return message


def send_message(chat_id, text="Default text"):
	url = URL + "sendMessage" + '?chat_id=' + str(chat_id) + "&text=" + str(text)
	# answer = {"char_id": chat_id, "text": text}
	r = requests.get(url)



def main():
	old_update_id = ''
	print('Bot Started')
	while True:
		message = get_message()
		if message['update_id'] != old_update_id:
			if 'q' in message['text'].lower():
				send_message(message["chat_id"], all_info())
			old_update_id = message['update_id']
		sleep(3)


if __name__ == '__main__':
	main()
