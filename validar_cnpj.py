def validar_cnpj(cnpj):
    # cnpj = '11.222.333/0001-81'

    # Aqui estou divindo o CNPJ para que eu consiga validar
    cnpj_dividido = cnpj.split('-')
    # print(cnpj_dividido)
    cnpj_digitos = cnpj_dividido[1]
    cnpj_numeros = cnpj_dividido[0]
    cnpj_divido_2 = cnpj_numeros.split('/')
    cnpj_numeros_2 = cnpj_divido_2[0].replace('.', '')
    cnpj_mil = cnpj_divido_2[1]

    # Irei dividir a validação em 2 fases para o calculo
    # Fase 1 irei calcular os 4 primeiros números em ordem descrescente de 5 a 2
    numeros_fase_1_digito_1 = cnpj_numeros_2[:4]

    soma_fase_1_digito_1 = 0
    multiplicador_fase_1_digito_1 = 5
    for i_fase_1_digito_1 in numeros_fase_1_digito_1:

        i_fase_1_digito_1 = int(i_fase_1_digito_1)
        soma_fase_1_digito_1 += i_fase_1_digito_1 * multiplicador_fase_1_digito_1

        multiplicador_fase_1_digito_1 -= 1

    numeros_fase_2_digito_1 = cnpj_numeros_2[4:] + cnpj_mil
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

    #  ------------------------ COMEÇANDO A VALIDAR O SEGUNDO DIGITO ---------------------------------
    numeros_fase_1_digito_2 = cnpj_numeros_2[:5]

    soma_fase_1_digito_2 = 0
    multiplicador_fase_1_digito_2 = 6
    for i_fase_1_digito_2 in numeros_fase_1_digito_2:

        i_fase_1_digito_2 = int(i_fase_1_digito_2)
        soma_fase_1_digito_2 += i_fase_1_digito_2 * multiplicador_fase_1_digito_2

        multiplicador_fase_1_digito_2 -= 1

    numeros_fase_2_digito_2 = cnpj_numeros_2[5:] + cnpj_mil + str(primeiro_digito)

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

    # VALIDAÇÃO DOS DIGITOS
    digitos_juntos = str(primeiro_digito) + str(segundo_digito)
    if digitos_juntos == cnpj_digitos:
        print('CNPJ Válido')
        print(50 * '-')
    else:
        print('CNPJ Inválido')
        print(50 * '-')
