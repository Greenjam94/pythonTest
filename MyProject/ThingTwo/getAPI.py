import requests

x = requests.get('https://pokeapi.co/api/v2/generation/2/')

print(x.text)