#Requisitos:
#Depositar apenas valores positivos
#O projeto trabalha apenas com 1 usuário
#Todas as operações devem ser exibidas no extrato
#Permite realizar 3 saques diários com limite máximo de R$ 500,00/saque
#Caso o usuário não tenha saldo o sistema deve exibir uma mensagem
#No final do extrato deve ser exibido o saldo atual da conta
#Os valores devem ser exibidos no formato R$ xxx.xx (exemplo: 1500.45)

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao =="d":
        valor =float(input( "Informe o valor do depósito: " ))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:   R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Valor inválido!!")
            
    elif opcao == "s":
        valor = float(input("informar o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação falhou!Você não tem saldo suficiente. Economize mais!!")

        elif excedeu_limite:
            print("Operação falhou!O valor do saque excedeu o limite. Gaste menos!!")

        elif excedeu_saques:
            print("Operação falhou!Número máximo de saques excedidos. DEixe a grana com a gente!!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:      R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "e":
        print("\n#############  E X T R A T O  #############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(f"Saldo:       R$ {saldo:.2f}")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("\n#############  Fim do Extrato #############")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada.")

