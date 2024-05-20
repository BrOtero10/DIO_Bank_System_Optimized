menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[i] Verificar Usuários
[l] Verificar Contas Corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas_corrente = []

def realizar_saque(*, valor, saldo, extrato):
    global numero_saques, LIMITE_SAQUES

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def realizar_deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito concluído com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def verificar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Digite os números de seu CPF: ")

    for user in usuarios:
        if user["cpf"] == cpf:
            print("CPF já cadastrado!")
            return False

    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")

    estado = input("Digite a sigla de seu estado: ")
    cidade = input("Digite o nome de sua cidade: ")
    bairro = input("Digite o nome de seu bairro: ")
    logradouro = input("Digite o nome de seu logradouro: ")
    numero = input("Digite o número de sua casa: ")

    endereco = f"{logradouro} - {numero} - {bairro} - {cidade}/{estado}"

    novo_usuario = {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}

    usuarios.append(novo_usuario)
    print("\nUsuário criado com sucesso!")
    return True

def criar_conta_corrente(usuarios, contas_corrente):
    cpf = input("Digite os números de seu CPF: ")

    isUser = False
    for user in usuarios:
        if user["cpf"] == cpf:
            isUser = True
            break
    
    if not isUser:
        print("\nUsuário não encontrado!")
        return False
    
    agencia = "0001"
    numero_conta = len(contas_corrente) + 1

    nova_conta_corrente = {"cpf_usuario": cpf, "agencia": agencia, "numero_conta": numero_conta}

    contas_corrente.append(nova_conta_corrente)
    print("\nConta corrente criada com sucesso!")
    return True

def verificar_usuarios(usuarios):
    if len(usuarios) > 0:
        for user in usuarios:
            print(f"Usuário: {user["nome"]} - CPF: {user["cpf"]}\nData de nascimento: {user["data_nascimento"]}\nEndereço: {user['endereco']}\n\n")
    else:
        print("\nNenhum usuário encontrado!")

def verificar_conta_corrente(contas_corrente):
    if len(contas_corrente) > 0:
        for conta in contas_corrente:
            print(f"Número da conta: {conta["numero_conta"]} - Agência: {conta["agencia"]}\nCPF do proprietário: {conta["cpf_usuario"]}\n\n")
    else:
        print("\nNenhuma conta corrente encontrada!")

while True:

    opcao = input(menu)
    print()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = realizar_deposito(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = realizar_saque(valor=valor, saldo=saldo, extrato=extrato)
        
    elif opcao == "e":
        verificar_extrato(saldo, extrato=extrato)
    
    elif opcao == "u":
        criar_usuario(usuarios)
    
    elif opcao == "c":
        criar_conta_corrente(usuarios, contas_corrente)

    elif opcao == "l":
        verificar_conta_corrente(contas_corrente)

    elif opcao == "i":
        verificar_usuarios(usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")