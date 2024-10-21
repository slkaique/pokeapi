# Finalidade
1. Desenvolver um script para realizar a extração de dados referente aos pokemons.
- Numero do pokemon (id)
- Nome do pokemon
- Area de localização 

# Link e Topicos importantes da documentação
- link: https://pokeapi.co/docs/v2#pokemon

1. get - https://pokeapi.co/api/v2/pokemon/{id or name}/
- Exemplo:   
    - id:35
    - name:"clefairy"
    - base_experience:113
    - height:6
    - is_default:true
    - order:56
    - weight:75

2. get - https://pokeapi.co/api/v2/pokemon/{id or name}/encounters
- Exemplo: 
    - name:"kanto-route-2-south-towards-viridian-city"
    - url:"https://pokeapi.co/api/v2/location-area/296/"

# Primeiros passos
1. Analisar o retorno de dados da API com o Postman;
2. Buscar os nome e id do pokemon;
3. Salvar o resultado em um DF;
4. Criar o loop do DF para buscar as areas do pokemon;
5. Verificar o fluxo de requisição;

# Bibliotecas 
1. Requests;
2. Pandas;

