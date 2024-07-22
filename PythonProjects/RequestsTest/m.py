import requests
import json

URL = 'https://api.pokemonbattle.ru'


HEADER = {
    'Content-Type': 'application/json',
    'Trainer_token': '0365668e7cee0b92df5df8fff514d3e8'
}

BODY = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=BODY, timeout=5) 
print(f'статус код: {response.status_code}. Сообщение: {response.text}')


import requests
import json

URL = 'https://api.pokemonbattle.ru'


HEADER = {
    'Content-Type': 'application/json',
    'Trainer_token': '0365668e7cee0b92df5df8fff514d3e8'
}

BODY = {
    "pokemon_id": "44513",
    "name": "Nort",
    "photo_id": 2
}

response = requests.put(url=f'{URL}/v2/pokemons', headers=HEADER, json=BODY, timeout=5) 
print(f'статус код: {response.status_code}. Сообщение: {response.text}')

import requests
import json

URL = 'https://api.pokemonbattle.ru'


HEADER = {
    'Content-Type': 'application/json',
    'Trainer_token': '0365668e7cee0b92df5df8fff514d3e8'
}

BODY = {
    "pokemon_id": "44516"
}

response = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers=HEADER, json=BODY, timeout=5) 
print(f'статус код: {response.status_code}. Сообщение: {response.text}')