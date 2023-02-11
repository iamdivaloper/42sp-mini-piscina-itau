#!/usr/bin/python3

class HotBeverage:
    # Define os atributos padrão para a classe HotBeverage
    price = 0.30
    name = "hot beverage"

    def description(self):
        # Retorna a descrição padrão para a bebida quente
        return "Just some hot water in a cup."

    def __str__(self):
        # Retorna uma representação em string da instância da classe HotBeverage
        return f"name: {self.name}\nprice: {'%.2f' % self.price}\ndescription: {self.description()}"


# Classe Coffee herda todas as propriedades e métodos da classe HotBeverage
class Coffee(HotBeverage):
    # Atualiza os valores dos atributos da classe HotBeverage para atender às necessidades de uma bebida de café
    price = 0.40
    name = "coffee"

    def description(self):
        # Retorna a descrição apropriada para a bebida de café
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"

class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

if __name__ == "__main__":
    # Instanciando a classe HotBeverage
    hot_beverage = HotBeverage()
    # Exibindo as informações da instância
    print(hot_beverage)

    coffee = Coffee()
    print(coffee)

    tea = Tea()
    print(tea)

    chocolate = Chocolate()
    print(chocolate)

    cappuccino = Cappuccino()
    print(cappuccino)
