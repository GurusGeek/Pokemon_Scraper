import requests
from bs4 import BeautifulSoup

url = 'https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', class_=['wikitable', 'rounded'])

pokemon_list = []

for table in tables:
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all('td')
        index = cols[0].text.strip()
        name = cols[2].text.strip()
        type1 = cols[3].text.strip()
        type2 = cols[4].text.strip()
        link = cols[1].find('a')['href']
        
        pokemon = {
            'index': index,
            'name': name,
            'type1': type1,
            'type2': type2,
            'url': f'https://pokemon.fandom.com/wiki/{name}'
        }
        
        pokemon_list.append(pokemon)
print(f"Total number of Pokémons: {len(pokemon_list)}")
for pokemon in pokemon_list[:10]:
    print(f"Name: {pokemon['name']}")
    print(f"Index: {pokemon['index']}")
    print(f"URL: {pokemon['url']}")
    print(f"Type 1: {pokemon['type1']}")
    print(f"Type 2: {pokemon['type2']}\n")
