import sys
import os
import re

def render(template_file, settings_file):
    # Carrega as configurações do arquivo de configurações
    with open(settings_file, "r") as f:
        settings = f.read()
    exec(settings)

    # Carrega o arquivo de template
    with open(template_file, "r") as f:
        template = f.read()

    # Substitui os marcadores no template pelos valores das configurações
    result = template
    locals_copy = locals().copy()
    for key in locals_copy.keys():
        if key != "template" and key != "result":
            result = re.sub("{{" + key + "}}", str(locals_copy[key]), result)

    # Grava o resultado em um arquivo com a extensão .html
    output_file = os.path.splitext(template_file)[0] + ".html"
    with open(output_file, "w") as f:
        f.write(result)

if __name__ == "__main__":
    # Verifica se o número de argumentos está correto
    if len(sys.argv) != 2:
       print("Error: Invalid number of arguments")
       print("Usage: python render.py template_file")
       sys.exit(1)

    # Verifica se o arquivo tem a extensão correta
    template_file = sys.argv[1]
    if os.path.splitext(template_file)[1] != ".template":
       print("Error: Invalid file extension")
       print("The file must have a '.template' extension")
       sys.exit(1)

    # Verifica se o arquivo existe
    if not os.path.isfile(template_file):
        print("Error: The file does not exist")
        sys.exit(1)

    # Verifica se o arquivo de configurações existe
    settings_file = "settings.py"
    if not os.path.isfile(settings_file):
        print("Error: The settings file does not exist")
        sys.exit(1)

    render(template_file, settings_file)
