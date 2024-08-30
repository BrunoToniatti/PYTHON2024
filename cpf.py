import os
import random

while True:
    print('## MENU ##')
    print('1 - Validar CPF')
    print('2 - Gerar CPF')
    print('0 - Sair')
    
    escolha = input('Escolha uma das opçoes: ')

    if escolha == '0':
        os.system('cls')
        print('Saindo...')
        break
    elif escolha == '1':
        os.system('cls')
        print('Digite um CPF no formato XXX.XXX.XXX-XX')
        cpf = input('-> ')

        cpf_separado = cpf.split('-')

        nove_digitos_separados = cpf_separado[0].split('.')

        nove_digitos_juntos = ''.join(nove_digitos_separados)
        # print(nove_digitos_juntos)



        multiplicador = 10
        soma_digitos = 0
        try:
            for digito in nove_digitos_juntos:
                digito_int = int(digito)
                multiplicacao = digito_int * multiplicador
                soma_digitos += multiplicacao
                multiplicador -= 1
            soma_mutiplicada = soma_digitos * 10
            resto_1 = soma_mutiplicada % 11
            primeiro_digito = 0 if resto_1 > 9 else resto_1
        except:
            print('CPF Inválido')
            print(50 * '-')
        try:
            dois_digitos_separados = cpf_separado[1]
            dez_digitos = nove_digitos_juntos + dois_digitos_separados[0]
            multiplicador_2 = 11
            soma_dez_digitos = 0
            for digito_2 in dez_digitos:
                try:
                    digito_2 = int(digito_2)
                except:
                    print('CPF Inválido')
                    print(50 * '-')
                soma_dez_digitos += digito_2 * multiplicador_2
                multiplicador_2 -= 1

            resto_2 = (soma_dez_digitos * 10) % 11
            segundo_digito = resto_2 if resto_2 <= 9 else 0

            digitos_validos = int(dois_digitos_separados[0]) == primeiro_digito and int(dois_digitos_separados[1]) == segundo_digito

            if digitos_validos:
                print('CPF Válido')
                print(50 * '-')
            else:
                print('Cpf Inválido')
                print(50 * '-')
        except:
            print('CPF Inválido')
            print(50 * '-')
    
    elif escolha == '2':

        os.system('cls')
        cpf_digitos = ''
        for i in range(9):
            cpf_digitos += str(random.randint(0,9))

        soma_digitos = 0
        multiplicador = 10
        for digito in cpf_digitos:
            digito = int(digito)
            soma_digitos += digito * multiplicador
            multiplicador -= 1

        primeiro_digito = (soma_digitos * 10) % 11
        primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

        cpf_digitos += str(primeiro_digito)
        # SEGUNDO DIGITO

        multiplicador_2 = 11
        soma_dez_digitos = 0
        for digito_2 in cpf_digitos:
            digito_2 = int(digito_2)
            soma_dez_digitos += digito_2 * multiplicador_2
            multiplicador_2 -= 1

            resto_2 = (soma_dez_digitos * 10) % 11
            segundo_digito = resto_2 if resto_2 <= 9 else 0

        cpf_digitos += str(segundo_digito)
        cpf = cpf_digitos[0:3] + "." + cpf_digitos[3:6] + "." + cpf_digitos[6:9] + "-" + cpf_digitos[9:]
        print('CPF GERADO:',cpf)
        print(50 * '-')



