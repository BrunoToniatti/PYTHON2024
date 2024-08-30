import os
import random

def gerar_cnpj():

    print('Para o CNPJ é uma empresa [P]rincipal ou [F]ilial?')
    empresa = input('-> ').lower()
    if empresa == 'p':
        os.system('cls')
        sequencia = '0001'
    elif empresa == 'f':
        os.system('cls')
        filial_numero = input('Qual o numero da filial: ')
        if filial_numero == '1':
            os.system('cls')
            print('Uma filial não pode conter o sequencial 0001')
            print('TENTE NOVAMENTE!!')
            print(50 * '-')
        else:
            print(50 * '-')
            sequencia = '000' + filial_numero
            print(sequencia)
    else:
        os.system('cls')
        print('Digite P para PRINCIPAL ou F para FILIAL')
        print(50 * '-')
        
    digitos = ''
    os.system('cls')
    for i in range(8):
        digitos += str(random.randint(1, 9))
    numeros_fase_1_digito_1 = digitos[:4]
    soma_fase_1_digito_1 = 0
    multiplicador_fase_1_digito_1 = 5
    for i_fase_1_digito_1 in numeros_fase_1_digito_1:
        i_fase_1_digito_1 = int(i_fase_1_digito_1)
        soma_fase_1_digito_1 += i_fase_1_digito_1 * multiplicador_fase_1_digito_1
        multiplicador_fase_1_digito_1 -= 1
    numeros_fase_2_digito_1 = digitos[4:] + sequencia
    # FASE 2 EU PEGO O RESTO E VOU MULTIPLICANDO COMEÇANDO COM 9 E ADICIONO OS 0001
    soma_fase_2_digito_1 = 0
    multiplicador_fase_2_digito_1 = 9
    for i_fase_2_digito_1 in numeros_fase_2_digito_1:
        i_fase_2_digito_1 = int(i_fase_2_digito_1)
        soma_fase_2_digito_1 += i_fase_2_digito_1 * multiplicador_fase_2_digito_1
        multiplicador_fase_2_digito_1 -= 1
    soma_total_digito_1 = soma_fase_1_digito_1 + soma_fase_2_digito_1
    divisao_digito_1 = soma_total_digito_1 % 11 if soma_total_digito_1 % 11 > 2 else 0
    if divisao_digito_1 == 0:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - divisao_digito_1
    #  ----------------------- COMEÇANDO A VALIDAR O SEGUNDO DIGITO ---------------------------------
    numeros_fase_1_digito_2 = digitos[:5]
    soma_fase_1_digito_2 = 0
    multiplicador_fase_1_digito_2 = 6
    for i_fase_1_digito_2 in numeros_fase_1_digito_2:
        i_fase_1_digito_2 = int(i_fase_1_digito_2)
        soma_fase_1_digito_2 += i_fase_1_digito_2 * multiplicador_fase_1_digito_2
        multiplicador_fase_1_digito_2 -= 1
    numeros_fase_2_digito_2 = digitos[5:] + sequencia + str(primeiro_digito)
    soma_fase_2_digito_2 = 0
    multiplicador_fase_2_digito_2 = 9
    for i_fase_2_digito_2 in numeros_fase_2_digito_2:
        i_fase_2_digito_2 = int(i_fase_2_digito_2)
        soma_fase_2_digito_2 += multiplicador_fase_2_digito_2 * i_fase_2_digito_2
        multiplicador_fase_2_digito_2 -= 1
    soma_total_digito_2 = soma_fase_1_digito_2 + soma_fase_2_digito_2
    divisao_digito_2 = soma_total_digito_2 % 11 if soma_total_digito_2 % 11 > 2 else 0
    if divisao_digito_2 == 0:
        segundo_digito = 0
    else:
        segundo_digito = 11 - divisao_digito_2
    digitos = digitos[0:2] + '.' + digitos[2:5] + '.' + digitos[5:8]
    cnpj = digitos + '/' + sequencia + '-' + str(primeiro_digito) + str(segundo_digito)
    print(cnpj)
    print(50 * '-')