#Desafio Otimizando o Sistema Bancário com Funções Python
#Objetivo Geral

#Desafio: Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar
#e visualizar histórico(extrato). Além disso, o sistema precisa criar duas novas funções: criar usuário(cliente do banco) e 
# criar conta corrente(vincular com usuário).


#Criar funções para as operações:

#Função Sacar(nomeados) - keyword only
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

#Função Depositar(posição) - positional only
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

#Função Visualizar Historico(Extrato) - positional only e keyword only
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


#Função criar usuário(Cliente do banco)
#O programa deve armazenar os usuários em  uma lista, um usuário é composto por:
#nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: 
#logradouro, nro - bairro -cidade/sigla estado. Deve ser armazenado somente os números do CPF.
#Não podemos cadastrar 2 usuários com o mesmo CPF.
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    cpf = cpf.strip()

    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    if usuario_existente:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")



#Função criar conta corrente(vincular com usuário)
#O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número de conta e usuário.
#O número da conta é sequencial, inicianl em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta,
#mas uma conta pertence a somente um usuário.
#Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado, por favor crie o usuário primeiro.")
        return None


AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[n] Nova conta
[l] Listar contas
[q] Sair
=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "n":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "l":
        for conta in contas:
            print("="*40)
            print(f"Agência: {conta['agencia']}")
            print(f"Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']['nome']}")
            print("="*40)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema bancário!")
        break

    else:
        print("Opção inválida, tente novamente.")
