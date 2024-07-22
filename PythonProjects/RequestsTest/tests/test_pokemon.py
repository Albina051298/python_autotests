import requests
import pytest 

URL = 'https://api.pokemonbattle.ru'
HEADER = {
    'Content-Type': 'application/json',
    'Trainer_token': '0365668e7cee0b92df5df8fff514d3e8'
}
TRAINER_id =4437

def test_status_code(): 
    response = requests.get(url=f'{URL}/v2/pokemons', params={'Trainer_id': TRAINER_id}) 
    assert response.status_code == 200
    
def test_name():
    response_get = requests.get(url=f'{URL}/v2/pokemons', params={'Trainer_id': TRAINER_id})
    assert response_get.json()["data"][0]["name"] == 'mudkip'
    