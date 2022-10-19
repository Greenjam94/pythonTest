import requests

x = requests.get('https://pokeapi.co/api/v2/generation/1/')

print(x.text)