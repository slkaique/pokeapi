import requests
import pandas as pd

def buscar_pokemom(limite=100):
    pagina = 0
    qtde_requisicoes = 0
    todos_pokemon = []

    while True:
        url = f"https://pokeapi.co/api/v2/pokemon?offset={pagina}&limit={limite}"
        response = requests.get(url)
        dados_pokemon = response.json()
        todos_pokemon.extend(dados_pokemon['results'])
        qtde_requisicoes += 1
        print(f' Numero de paginas processadas:{qtde_requisicoes}')

        # Verifica se há mais resultados
        if not dados_pokemon['results']:
            break

        pagina += limite

    return todos_pokemon

def buscar_localizacao(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/encounters"
    response = requests.get(url)
    if response.status_code == 200:
        locais = response.json()
        return [local['location_area']['name'] for local in locais]
    else:
        return []
    
lista_pokemon = buscar_pokemom()
df = pd.DataFrame(lista_pokemon)
ids = []

for pokemon in lista_pokemon:
    id = pokemon['url'].split('/')[-2]
    ids.append(int(id))

df['id'] = ids
lista_final = []

for _, row in df.iterrows():
    pokemon_id = row['id']
    nome = row['name']
    locais = buscar_localizacao(pokemon_id)

    if locais:
        for local in locais:
            lista_final.append({'id': pokemon_id, 'name': nome, 'location_area': local})
    else:  
        lista_final.append({'id': pokemon_id, 'name': nome, 'location_area': 'Desconhecido'})

df_final = pd.DataFrame(lista_final)

df_final.to_csv('area_pokemon.csv',index=False)