import requests

response = requests.get('https://api.sampleapis.com/switch/games')

API_Data = response.json()

print("First game ID:", API_Data[0]['id'])

for game in API_Data:
    game_name = game["name"]
    print("Game name:", game_name)


