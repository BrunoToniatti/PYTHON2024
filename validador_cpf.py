"""
Validador de CPF, multiplicar todos os valores antes dos digitos em contagem regreciva
511.306.658

1 - 5x10 1x9 1x8...
2 - Precisamos somar o valor total 
3 - Multiplicamos o valor total por 10
4 - Pegamos o resto da divisão por 11 do valor total * 10,
se der mais que 9 então ele é 0
"""
def validar_cpf(cpf):

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
        print(50 * '#')
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
                print(50 * '#')
            soma_dez_digitos += digito_2 * multiplicador_2
            multiplicador_2 -= 1

        resto_2 = (soma_dez_digitos * 10) % 11
        segundo_digito = resto_2 if resto_2 <= 9 else 0

        digitos_validos = int(dois_digitos_separados[0]) == primeiro_digito and int(dois_digitos_separados[1]) == segundo_digito

        if digitos_validos:
            print('CPF Válido')
            print(50 * '#')
        else:
            print('Cpf Inválido')
            print(50 * '#')
    except:
        print('CPF Inválido')
        print(50 * '#')

# Segundo digito

