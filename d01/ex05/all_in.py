import sys

# Cria dicionários para estados e capitais
def create_dicts():
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}
    
    # Retorna os dicionários de estados e capitais
    return states, capital_cities

# Encontra a capital correspondendo ao estado fornecido como argumento
def find_capital(arg, states, capitals):
    # Converte o argumento para título e minúsculas
    arg = arg.lower().title()
    # Pega a abreviação do estado usando o argumento
    abbreviate_state = states.get(arg)
    if abbreviate_state:
        # Pega a capital usando a abreviação do estado
        capital = capitals.get(abbreviate_state)
        if capital:
            # Retorna o estado e a capital correspondentes
            return arg, capital
    # Retorna None se não encontrar o estado ou capital correspondente
    return None

# Encontra o estado correspondente à cidade capital fornecida como argumento
def find_state(arg, states, capitals):
    # Converte o argumento para minúsculas
    arg = arg.lower()
    # Loop através do dicionário de capitais
    for state, city in capitals.items():
        # Verifica se a cidade corresponde ao argumento
        if city.lower() == arg:
            # Pega a abreviação do estado
            abbreviate_state = state
            # Encontra o nome do estado correspondente usando a abreviação
            state_name = [k for k, v in states.items() if v == abbreviate_state][0]
            # Retorna o nome do estado e a cidade correspondentes
            return state_name, city

    # Retorna None se não encontrar o estado ou cidade correspondente
    return None

# Função principal que processa todos os argumentos
def all_in():
    # Verifica se foi fornecido um único argumento
    if len(sys.argv) == 2:
        # Divide o argumento em uma lista de strings
        args = sys.argv[1].split(",")
        # Remove os espaços em branco de cada string
        args = [arg.strip() for arg in args]
        # Cria dicionários de estados e capitais
        states, capitals = create_dicts()
        # Loop através da lista de argumentos
        for arg in args:
            # Ignora argumentos vazios
            if not arg:
                continue
            # Encontra o estado ou capital correspondente ao argument
            result = find_state(arg, states, capitals) or find_capital(arg, states, capitals)
            # Verifica se existe algum resultado, se existir,
            if result:
                # desempacota o resultado para state e capital
                state, capital = result
                 # imprime a mensagem com a capital e o estado formatados
                print("{} is the capital of {}".format(capital, state))
            # Se não houver resultado, 
            else:
                # imprime uma mensagem informando que a string informada não é nem uma cidade capital nem um estado
                print("{} is neither a capital city nor a state".format(arg))

if __name__ == "__main__":
    all_in()
