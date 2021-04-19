import json
import requests

response = requests.get('https://api.dccresource.com/api/games')
game_data = response.json()