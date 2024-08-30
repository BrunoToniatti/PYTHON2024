"""
Criar uma lista de compras que consiga:
Inserir, apagar e listar
"""

import os

lista = []

while True:
    print('Escolha uma das opções')
    print('1 - Listar')
    print('2 - Incluir')
    print('3 - Apagar')
    print('0 - Sair')
    
    escolha = input('Escolha: ')

    try:
        escolha = int(escolha)
    except:
        print('Escolha um valor válido')
        continue

    if escolha == 0:
        os.system('cls')
        print('Saindo...')
        break
    
    elif escolha == 1:
        os.system('cls')
        if lista == []:
            print(50 * '-')
            print('A lista esta vazia')
            print(50 * '-')
        else:
            print(50 * '-')
            print('Itens para comprar: ')
            for indice, nome in enumerate(lista):
                print(indice, nome)
            print(50 * '-')
    elif escolha == 2:
        os.system('cls')
        produto = input('O que comprar: ')
        if produto == '':
            os.system('cls')
            print('Você precisa informar um produto ')
            continue
        else:
            os.system('cls')
            lista.append(produto)
            print('Item adicionado com sucesso')
            continue
    elif escolha == 3:
        if lista == []:
            os.system('cls')
            print('A lista está vazia!!')
            continue
        else:
            os.system('cls')
            for indice, nome in enumerate(lista):
                print(indice, nome)
            indice = input('Informe o número do produto que você deseja retirar: ')
            try:
                indice = int(indice)
            except:
                os.system('cls')
                print('O indice precisa ser um número')
                continue
            
            try:
                os.system('cls')
                lista.pop(indice)
                print('Item retirado da lista')
            except:
                os.system('cls')
                print('Escolha um indice válido')
        