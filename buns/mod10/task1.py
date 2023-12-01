import requests
import json

starships_data = json.loads(requests.get('https://swapi.dev/api/starships/').text)
people_page_2_data = json.loads(requests.get('https://swapi.dev/api/people/?page=2').text)
people_page_3_data = json.loads(requests.get('https://swapi.dev/api/people/?page=3').text)
planet_14 = json.loads(requests.get('https://swapi.dev/api/planets/14/').text)
planet_22 = json.loads(requests.get('https://swapi.dev/api/planets/22/').text)
planet_30 = json.loads(requests.get('https://swapi.dev/api/planets/30/').text)
planet_33 = json.loads(requests.get('https://swapi.dev/api/planets/33/').text)

new_ships_data = {}

for starship in starships_data['results']:
    if starship['name'] == 'Millennium Falcon':
        new_starship = {'name': starship['name'],
                        'max_atmosphering_speed': starship['max_atmosphering_speed'],
                        'starship_class': starship['starship_class'],
                        'pilots': []}

        for pilot_url in starship['pilots']:
            for person in people_page_2_data['results'] + people_page_3_data['results']:
                if person['url'] == pilot_url:
                    new_pilot = {key: person[key] for key in ['name', 'height', 'mass', 'homeworld']}
                    new_pilot['homeworld-url'] = person['homeworld']
                    for planet_code in [planet_14, planet_22, planet_30, planet_33]:
                        if person['homeworld'] == planet_code['url']:
                            new_pilot['homeworld'] = planet_code['name']
                    new_starship['pilots'].append(new_pilot)
        new_ships_data.update(new_starship)

with open('ships.json', 'w') as file:
    json.dump(new_ships_data, file, indent=4)



