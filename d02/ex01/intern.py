class Intern:
    # Inicialização da classe Intern
    # name é um parâmetro opcional, com valor padrão "My name? I’m nobody, an intern, I have no name."
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        # Atribuindo o nome ao atributo Name
        self.Name = name
        
    # Método para representação do objeto como string
    def __str__(self):
        # Retorna o valor do atributo Name
        return self.Name
    
    # Classe aninhada Coffee
    class Coffee:
        # Método para representação do objeto como string
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    # Método para o trabalho
    def work(self):
        # Levanta uma exceção com a mensagem "I’m just an intern, I can’t do that..."
        raise Exception("I’m just an intern, I can’t do that...")
        
    # Método para fazer café
    def make_coffee(self):
        # Retorna uma instância da classe Coffee
        return self.Coffee()

try:
    # Criando uma instância da classe Intern sem especificar o nome
    intern1 = Intern()
    # Exibindo o nome do estagiário
    print("Intern 1:", intern1)
    
    # Criando uma instância da classe Intern com o nome "Mark"
    intern2 = Intern(name="Mark")
    # Exibindo o nome do estagiário
    print("Intern 2:", intern2)
    
    # Pedindo a Mark para fazer um café
    coffee = intern2.make_coffee()
    # Exibindo o resultado
    print("Coffee:", coffee)
    
    # Pedindo para o outro estagiário trabalhar
    intern1.work()
except Exception as e:
    # Capturando a exceção levantada pelo método work() e exibindo sua mensagem
    print(e)

