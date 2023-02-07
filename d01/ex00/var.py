var_list = [42, '42', 'quarante-deux', 42.0,
            True, [42], {42: 42}, (42,), set()]


def my_var(valor):
    for i in valor:
        print(i, 'has a type', type(i))

# Verifica se o módulo corrente é o módulo principal
# Isso é feito para evitar que o código seja executado quando importado como um módulo
# Se o módulo corrente for o módulo principal, executa a função
if __name__ == '__main__':
    my_var(var_list)
