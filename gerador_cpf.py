"""
GERADOR DE CPF
rando.randint(0, 10) -> vai imprimir valores de 0 até 10 aleatóriamente
"""
import random

def gerar_cpf():
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
        try:
            digito_2 = int(digito_2)
        except:
            print('CPF Inválido')
        soma_dez_digitos += digito_2 * multiplicador_2
        multiplicador_2 -= 1

        resto_2 = (soma_dez_digitos * 10) % 11
        segundo_digito = resto_2 if resto_2 <= 9 else 0

    cpf_digitos += str(segundo_digito)
    cpf = cpf_digitos[0:3] + "." + cpf_digitos[3:6] + "." + cpf_digitos[6:9] + "-" + cpf_digitos[9:]

    print(cpf)
    print(50 * '-')


