
""" EJERCICIO """

import requests

""" try:
    response = requests.get('https://www.uva.es')
    print(response.status_code)
    print(response.headers['content-type'])
    print(response.text)           # Raw response body as a string
except requests.exceptions.RequestException as e:
    print(f"Error: {e}") """

""" EXTRA """

def pokemon_info(pokemon: str) -> None:
    
    try:
        response = requests.get(f"http://pokeapi.co/api/v2/pokemon/{pokemon}", timeout=5)
        if response.status_code == 200:
            show_pokemon_info(response.json())
           
            response = requests.get(f"http://pokeapi.co/api/v2/pokemon-species/{pokemon}", timeout=5)
            
            if response.status_code == 200:
                evolution_url = response.json()['evolution_chain']['url']
                
                response = requests.get(evolution_url, timeout=5)

                if response.status_code == 200:
                    show_pokemon_evolution(response.json())
                
                else:
                    print(f"Se ha producido el error: {response.status_code}")
            else:
                print(f"Se ha producido el error: {response.status_code}")
        else:
            print(f"No existe el pokemon {pokemon}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
def show_pokemon_info(data: str) -> None:
    
    print(f"El nombre del pokemon es: {data['name']}")
    print(f"El id del pokemon es: {data['id']}")
    print(f"El peso del pokemon es: {data['weight']}")
    print(f"La altura del pokemon es: {data['height']}")
    print(f"Este pokemon es del tipo(s): {[item['type']['name'] for item in data['types']]}")
    print(f"Este pokemon ha participado en los juegos: {[item['version']['name'] for item in data['game_indices']]}")

def show_pokemon_evolution(data: str) -> None:
    
    evolution_string = get_evolution_names(data['chain'])
    print(f"Cadena de evolución: {evolution_string}")
    
def get_evolution_names(chain):
    names = [chain['species']['name']]
    for evolution in chain.get("evolves_to", []):
        names.extend(get_evolution_names(evolution))
    return names


def main():
    
    pokemon_user = str(input("Introduce el nombre o id del pokemon a buscar: ")).lower()
    pokemon_info(pokemon_user)
    

if __name__ == "__main__":
    main()

