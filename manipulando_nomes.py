#Atividade - Manipulando Nomes em Python

cont_char = lambda x: len(x.replace(' ', ''))
reverse_string = lambda x: x[::-1]


while True:
    nome_completo = input('Digite seu nome completo: ')
    if nome_completo.replace(' ', '').lower() == 'sair': break

    nomes = [nome for nome in nome_completo.split(' ') if nome != '']
    for idx, nome in enumerate(nomes):
        saida = f'''
    Nome {idx + 1}: {nome}
    - Número de caracteres: {cont_char(nome)}
    - Posição: {idx + 1}
    - Invertido: {reverse_string(nome)}'''
        print(saida)
    print(end='\n\n')