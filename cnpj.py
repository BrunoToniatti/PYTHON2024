import gerador_cnpj
import validar_cnpj
import validador_cpf
import gerador_cpf
import os


while True:
    print('Escolha uma das opções')
    print('1 - Gerar CNPJ')
    print('2 - Validar CNPJ')
    print('3 - Gerar CPF')
    print('4 - Validar CPF')
    escolha = input('-> ')

    if escolha == '1':
        os.system('cls')
        gerador_cnpj.gerar_cnpj()

    elif escolha == '2':
        os.system('cls')
        print('Digite um CNPJ com a mascara XX.XXX.XXX/XXXX-XX')
        cnpj = input('> ')
        validar_cnpj.validar_cnpj(cnpj)
    elif escolha == '3':
        os.system('cls')
        gerador_cpf.gerar_cpf()
    elif escolha == '4':
        os.system('cls')
        print('Digite um CPF com a mascara XXX.XXX.XXX-XX')
        cpf = input('> ')
        print(50 * '-')
        validador_cpf.validar_cpf(cpf)