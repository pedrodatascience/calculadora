#Entrada de dados


print("UMA DICA!!!!!!!!!!\n é para utilizar os sinais '+', '-', '/' e '*' para realizar as operações\n")

operacao = input("Digite a operacao desejada: ")

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))


while True:
    if operacao == '+':
        print(float(numero1+numero2))
    elif operacao == '-':
        print(float(numero1-numero2))
    elif operacao == '/':
        print(float(numero1/numero2))
    elif operacao == '*':
        print(float(numero1*numero2))
    else:
        print('vc digitou algum comando errado')
    
    pergunta = str.lower(input('deseja fazer outra operação (s/n)?: '))
    if pergunta == 's':
        pass
    else:
        break
    break


#iniciando o loop
while True:
    #Opções do Usuário
    print("CALCULADORA PYTHON")
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')
    print('5 - SAIR DO PROGRAMA')


    #operação escolhida
    operacao = input('Operação deseja: ')

    #verifica se o usuário vai fazer o cálculo ou sair do programa
    if operacao != '5':
        #informa o numero
        x = str(input('Informe o 1° número: ')).replace(',','.')
        y = str(input('Informe o 2° número: ')).replace(',','.')

        #converte para float
        x = float(x)
        y = float(y)

        #verifica a opcao desejada
        match operacao:
            case '1':
                result = x + y
            case '2':
                result = x - y
            case '3':
                result = x / y
            case '4':
                result
    
