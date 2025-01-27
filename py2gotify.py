# Script to send message to Gotify Room
import argparse
import requests

parser = argparse.ArgumentParser(description='Send Message to Gotify.')
parser.add_argument('-s', '--server', help='Gotify Server Name', required=True)
parser.add_argument('-T', '--token', help='Enter room token', required=True)
parser.add_argument('-t', '--title', help='Write a nice title for your message', required=True)
parser.add_argument('-m', '--message', help='Write a nice message to send', required=True)

args = parser.parse_args()
TITLE = args.title
MESSAGE = args.message
TOKEN = args.token
SERVER = args.server

URL = f'https://{SERVER}/message?token={TOKEN}'
JSON = {'title': TITLE,
        'message': MESSAGE,
        'priority': 5}
SEND = requests.post(url = URL, json = JSON)

print(SEND.text)
