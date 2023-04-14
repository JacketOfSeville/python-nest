import requests

# Função para fazer a solicitação à PokeAPI
def obter_dados_pokemon(nome_ou_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_ou_id}"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        nome = dados['name']
        tipos = [tipo['type']['name'] for tipo in dados['types']]
        evolucao_url = dados['species']['url']
        evolucao_response = requests.get(evolucao_url)
        if evolucao_response.status_code == 200:
            evolucao_dados = evolucao_response.json()
            evolucoes = []
            if 'evolves_from_species' in evolucao_dados:
                evolucao_anterior = evolucao_dados['evolves_from_species']['name']
                evolucoes.append(evolucao_anterior)
            if 'evolution_chain' in evolucao_dados:
                evolucao_cadeia = evolucao_dados['evolution_chain']['url']
                evolucao_cadeia_response = requests.get(evolucao_cadeia)
                if evolucao_cadeia_response.status_code == 200:
                    evolucao_cadeia_dados = evolucao_cadeia_response.json()
                    evolucoes_proximas = evolucao_cadeia_dados['chain']
                    while evolucoes_proximas:
                        evolucao_atual = evolucoes_proximas['species']['name']
                        evolucoes.append(evolucao_atual)
                        if 'evolves_to' in evolucoes_proximas:
                            evolucoes_proximas = evolucoes_proximas['evolves_to'][0]
                        else:
                            evolucoes_proximas = None
            return nome, tipos, evolucoes
    else:
        print("Não foi possível obter os dados do Pokémon.")
        return None

# Função para exibir os dados do Pokémon
def exibir_dados_pokemon(nome, tipos, evolucoes):
    if nome and tipos and evolucoes:
        print("Nome:", nome)
        print("Tipos:", ", ".join(tipos))
        print("Evoluções:", ", ".join(evolucoes))
    else:
        print("Pokémon não encontrado.")

# Entrada do nome ou ID do Pokémon
nome_ou_id = input("Digite o nome ou ID do Pokémon: ")
dados_pokemon = obter_dados_pokemon(nome_ou_id)
exibir_dados_pokemon(*dados_pokemon)