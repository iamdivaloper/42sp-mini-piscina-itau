#!/usr/bin/python3

import random

from beverages import Cappuccino, Chocolate, Coffee, HotBeverage, Tea


class CoffeeMachine:
    def __init__(self):
        self.servings = 0  # contagem de bebidas servidas

    class EmptyCup(HotBeverage):
        # classe derivada de HotBeverage
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
            self.description = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        # classe de exceção herdada de Exception,
        def __init__(self):
            self.message = "This coffee machine has to be repaired."
            super().__init__(self.message)

    def repair(self):
        # método para consertar a máquina
        self.servings = 0

    def serve(self, drink_class):
        # método para servir bebidas
        if self.servings == 10:
            raise self.BrokenMachineException()  # lança uma exceção após servir 10 bebidas
        self.servings += 1
        if random.randint(0, 1) == 1:
            return drink_class()  # retorna uma bebida aleatória
        else:
            return self.EmptyCup()  # retorna um copo vazio aleatório


if __name__ == "__main__":
    # criação da instância da máquina de café
    cm = CoffeeMachine()
    try:
        # loop para servir bebidas até que a máquina quebre
        while True:
            for i in range(10):
            # seleção aleatória de uma bebida da lista disponíveis
                drink = cm.serve(random.choice(
                    [HotBeverage, Coffee, Tea, Chocolate, Cappuccino]))
                print("{} Serving: {}".format(i,drink.name))
    except CoffeeMachine.BrokenMachineException as bme:
        # gerenciamento da exceção de máquina quebrada
        print(bme.message)
        cm.repair()  # conserta a máquina
