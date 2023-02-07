d = {
    'Hendrix': '1942',
    'Allman': '1946',
    'King': '1925',
    'Clapton': '1945',
    'Johnson': '1911',
    'Berry': '1926',
    'Vaughan': '1954',
    'Cooder': '1947',
    'Page': '1944',
    'Richards': '1943',
    'Hammett': '1962',
    'Cobain': '1967',
    'Garcia': '1942',
    'Beck': '1944',
    'Santana': '1947',
    'Ramone': '1948',
    'White': '1975',
    'Frusciante': '1970',
    'Thompson': '1949',
    'Burton': '1939',
}

sorted_musicians = sorted(d.items(), key=lambda x: (x[1], x[0]))

for musician in sorted_musicians:
    print(musician[0])

# A solução começa ordenando o dicionário d pelos valores (anos de nascimento dos músicos), 
# e depois pelas chaves (nomes dos músicos) em caso de empate. 
# A lista ordenada de tuplas é armazenada em sorted_musicians, 
# e a solução percorre esta lista para imprimir os nomes dos músicos na ordem desejada.
