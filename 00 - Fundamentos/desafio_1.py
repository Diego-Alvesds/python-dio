#Desafio_1(Sistema Bancario Simples) Bootcamp Suzano - Python Developer

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
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")      
        valor = float(input("Informe o valor a ser depositado: "))
        if valor <= 0:
            print("Valor inválido, informe um valor positivo.")
        else:
            saldo += valor
            extrato += (f"Deposito: R${saldo:.2f}\n")

    elif opcao == "s":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:           
            valor_saque = float(input("Informe o valor a ser sacado: "))
            if valor_saque > limite:
                print(f"Não é possivel realizar o saque de R${valor_saque:.2f}, o limite maximo por saque é de R${limite:.2f}.")
            elif valor_saque > saldo:
                print("Não é possivel sacar o dinheiro por falta de saldo")
            else: 
                saldo -= valor_saque
                numero_saques += 1
                extrato += (f"Saque: R${valor_saque:.2f}\n")
        else:
            print("Você atingiu o limite de saques diários!")
           
           
    elif opcao == "e":
        print("Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"O seu saldo é atual de R${saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
            
