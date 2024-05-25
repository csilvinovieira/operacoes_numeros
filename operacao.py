def calculadora()
    while True
        print(Escolha uma operação)
        print(1 Soma)
        print(2 Subtração)
        print(3 Multiplicação)
        print(4 Divisão)
        print(0 Sair)

        opcao = input(Digite o número da operação desejada )

        if opcao == 0
            print(Encerrando a calculadora.)
            break
        elif opcao in (1, 2, 3, 4)
            try
                valor1 = float(input(Digite o primeiro valor ))
                valor2 = float(input(Digite o segundo valor ))
            except ValueError
                print(Valores inválidos. Certifique-se de inserir números válidos.)
                continue

            if opcao == 1
                resultado = valor1 + valor2
                print(fResultado da soma {resultado})
            elif opcao == 2
                resultado = valor1 - valor2
                print(fResultado da subtração {resultado})
            elif opcao == 3
                resultado = valor1  valor2
                print(fResultado da multiplicação {resultado})
            elif opcao == 4
                if valor2 != 0
                    resultado = valor1  valor2
                    print(fResultado da divisão {resultado})
                else
                    print(Não é possível dividir por zero.)
        else
            print(Essa opção não existe. Tente novamente.)

calculadora()