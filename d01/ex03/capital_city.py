import sys


def get_states(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    return states.get(state)


def get_capital_cities(city):
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    return capital_cities.get(city)


def display_states():
    # sys.argv para obter os argumentos de linha de comando
    if len(sys.argv) == 2: 
        city = get_states(sys.argv[1])
        if city == None:
            print('Unknown state')
        else:
            print(get_capital_cities(city))


if __name__ == '__main__':
     display_states()