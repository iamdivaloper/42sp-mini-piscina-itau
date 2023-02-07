import sys


def get_states(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    # Usar o método next para procurar;
    return next((key for key, value in states.items() if value == state), None)


def get_capital_cities(city):
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    return next((key for key, value in capital_cities.items() if value == city), None)



def display_capital_cities():
    # sys.argv para obter os argumentos de linha de comando
    if len(sys.argv) == 2:  
        city = get_capital_cities(sys.argv[1])
        if city is None:
            print('Unknown capital city')
        else:
         print(get_states(city))
        

if __name__ == '__main__':
    display_capital_cities()
